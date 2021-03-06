#!/usr/bin/env python3
# jobs.py
# Main script
import datetime
import os

import gspread

from dotenv import load_dotenv
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

SPREADSHEET_KEY = os.getenv("SPREADSHEET_KEY")
SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH")

google_sheets_connection = gspread.service_account(filename=SERVICE_ACCOUNT_PATH)
spreadsheet = google_sheets_connection.open_by_key(SPREADSHEET_KEY)

ENTRY_LEVEL_HIGHLIGHT = {
    "red": 52 / 255,
    "green": 168 / 255,
    "blue": 83 / 255,
}

WHITE_BACKGROUND_COLOR = {"red": 1.0, "green": 1.0, "blue": 1.0}

# TODO: Create a class to hold the spreadsheet to be passed to functions


class JobPosting:
    """Class to contain information relating to job postings."""

    def __init__(self, title, company, url):
        self._title = title
        self._company = company
        self._url = url

    def spreadsheet_format(self):
        return [self._title, self._company, self._url]


def get_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=chrome_options)


# Acquire company webpages from google sheet configuration tab
# {"company":.., "url":.., "selector":..}
def acquire_webpages():
    config_ws = spreadsheet.worksheet("Configuration")
    companies = config_ws.get_all_records()
    return companies


# Returns a dictionary of lists of JobPostings parsed from each company website
# Keys are disciplines
def acquire_job_postings(company_dict_list):
    jobs = {
        "Animation": [],
        "Art": [],
        "Audio": [],
        "Design": [],
        "Production": [],
        "Programming": [],
        "Misc": [],
    }

    # TODO: Potentially acquire webpages async to avoid slow scripts
    for c in company_dict_list:
        logger.info(f"[{c['company']}] Acquiring jobs...")
        # Acquire html text of company career page
        # TODO: Check response status
        webpage_jobs = parse_jobs_page(c["url"], c["selector"])

        if not webpage_jobs:  # No jobs found
            logger.info(f"[{c['company']}] No jobs found.")
            continue

        # Append jobs to aggreggated list
        for jt in filter_jobs(webpage_jobs):
            discipline = categorize_job(jt)
            jobs[discipline].append(JobPosting(jt, c["company"], c["url"]))

    return jobs


# TODO: Re-use driver for performance
def parse_jobs_page(url, selector):
    job_titles = []
    driver = get_webdriver()
    driver.get(url)
    try:
        job_web_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )
        job_titles = [web_element.text for web_element in job_web_elements]
        logger.debug(job_titles)
    except:
        logger.error(f"Timeout occured for url: {url}")
    finally:
        return job_titles


# Filters out irrelevant job postings such as senior positions
def filter_jobs(job_title_list):
    excluded_keywords = [
        "director",
        "executive",
        "lead",
        "manager",
        "principal",
        "senior",
        "m.s.",
        "ph.d",
        "mba",
    ]

    filtered_list = []

    for title in job_title_list:
        if not any(kw in title.lower() for kw in excluded_keywords):
            filtered_list.append(title)

    return filtered_list


def categorize_job(job_title):
    # NOTE: Ordered to avoid false positives (e.g. "design" in "sound designer")
    discipline_keywords = {
        "Production": ["producer", "project manager", "product manager", "production"],
        "Animation": ["animation", "animator", "rigger", "rigging"],
        "Art": ["art", "artist", "vfx"],
        "Audio": ["sound designer", "composer", "sound", "audio", "sfx"],
        "Design": ["design", "designer"],
        "Programming": [
            "coder",
            "developer",
            "engineer",
            "engineering",
            "programmer",
            "programming",
        ],
    }

    for discipline, keywords in discipline_keywords.items():
        if any(kw in job_title.lower() for kw in keywords):  # Any keywords in job title
            return discipline

    # Doesn't match any disciplines
    return "Misc"


def update_job_sheet(worksheet, updated_jobs):
    clear_worksheet(worksheet)
    if not updated_jobs:
        print(f"Jobs for {worksheet.title} is empty. Skipping..")
        return

    last_row_num = len(updated_jobs) + 1  # Header offset
    worksheet.update(
        f"A2:C{last_row_num}", [j.spreadsheet_format() for j in updated_jobs]
    )
    highlight_entry_level_postings(worksheet)

    logger.success(f"{worksheet.title} worksheet updated.")


def clear_worksheet(worksheet):
    clear_highlighting(worksheet)
    num_rows = len(worksheet.col_values(1)) - 1
    if num_rows > 0:
        logger.info(f"Cleared {worksheet.title}!A2:G{1+num_rows}")
        spreadsheet.values_clear(f"{worksheet.title}!A2:G{1+num_rows}")


# TODO: Ensure highlighting is cleared for empty rows
def clear_highlighting(worksheet):
    num_rows = len(worksheet.col_values(1)) - 1
    if num_rows > 0:  # No job entries
        worksheet.format(
            f"A2:G{1+num_rows}", {"backgroundColor": WHITE_BACKGROUND_COLOR}
        )
        logger.debug(f"Cleared highlighting for {worksheet.title}!A2:G{1+num_rows}")


def highlight_entry_level_postings(worksheet):
    for row_num, job_title in enumerate(
        worksheet.col_values(1)[1:], start=2
    ):  # Omit header
        # FIXME: Change to bulk update to avoid exceeding max request limit
        if is_entry_level(job_title):
            worksheet.format(
                f"A{row_num}:G{row_num}", {"backgroundColor": ENTRY_LEVEL_HIGHLIGHT}
            )


@logger.catch
def is_entry_level(job_title):
    ENTRY_LEVEL_KEYWORDS = [
        "associate",
        "assistant",
        "junior",
        "intern",
        "internship",
        "entry",
    ]
    return any(kw in job_title.lower() for kw in ENTRY_LEVEL_KEYWORDS)


##############################################################################
################################# SCRIPT BODY ################################
##############################################################################
# @logger.catch  # Catch & log all errors
if __name__ == "__main__":
    # Acquire webpages
    company_dicts = acquire_webpages()

    # Get job postings from webpages
    all_jobs = acquire_job_postings(company_dicts)

    # Update spreadsheet with postings
    for k in all_jobs.keys():
        update_job_sheet(spreadsheet.worksheet(k), all_jobs[k])

    logger.success("Spreadsheet updated.")
    print(f"Spreadsheet was successfully updated.")

    # Mark update in spreadsheet
    info_ws = spreadsheet.worksheet("INFO")
    time_now = datetime.datetime.now().strftime(f"%m/%d %I:%M:%S %p")
    info_ws.update("A2", f"Last Updated: {time_now} (GMT-5)")
