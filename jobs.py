#!/usr/bin/env python3
# jobs.py
# Main script
import os

import gspread
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# FIXME: Change back to production spreadsheet key
# SPREADSHEET_KEY = os.getenv("SPREADSHEET_KEY")
SPREADSHEET_KEY = os.getenv("DEV_SPREADSHEET_KEY")

SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH")

gc = gspread.service_account(filename=SERVICE_ACCOUNT_PATH)
spreadsheet = gc.open_by_key(SPREADSHEET_KEY)


class JobPosting:
    """Class to contain information relating to job postings."""

    def __init__(self, title, company, url):
        self._title = title
        self._company = company
        self._url = url

    def spreadsheet_format(self):
        return [self._title, self._company, self._url]


# Acquire company webpages from google sheet configuration tab
# {"company":.., "url":.., "attribute":.., "attr_val":..}
def acquire_webpages():
    # TODO: Implement this function
    config_ws = spreadsheet.worksheet("Configuration")
    companies = config_ws.get_all_records()
    return companies


# Returns a list of JobPostings parsed from the webpage text
def acquire_job_postings(company_dict: dict):
    webpage_html = requests.get(company_dict["url"]).text
    soup = BeautifulSoup(webpage_html, "html.parser")

    attr_dict = {company_dict["attribute"]: company_dict["attr_val"]}
    job_titles = [entry.string.strip() for entry in soup.find_all(attrs=attr_dict)]

    jobs = []
    for jt in job_titles:
        jobs.append(JobPosting(jt, company_dict["company"], company_dict["url"]))

    return jobs


# Filters out irrelevant job postings such as senior positions
def filter_jobs(job_list):
    # TODO: Implement this function
    raise NotImplementedError


def update_job_sheet(worksheet_name, updated_jobs):
    ws = spreadsheet.worksheet(worksheet_name)
    last_row_num = len(updated_jobs) + 1  # Header offset
    print(f"Last row number: {last_row_num}")
    ws.update(f"A2:C{last_row_num}", [j.spreadsheet_format() for j in updated_jobs])


##############################################################################
################################# SCRIPT BODY ################################
##############################################################################
if __name__ == "__main__":
    # Acquire webpages
    company_webpage_list = acquire_webpages()

    all_job_postings = []
    # Get job postings from webpages
    for c in company_webpage_list:
        company_jobs = acquire_job_postings(c)
        all_job_postings.extend(company_jobs)

    update_job_sheet("Production", all_job_postings)

    # Filter job postings

    # Update spreadsheet with postings
