#!/usr/bin/env python3
# jobs.py
# Main script
from bs4 import BeautifulSoup


# Returns the list of job positions within the webpage text
# css_attrs is used to identify how job titles are formatted in the html doc
# css_attrs = "<css_attribute>" : "<attribute_value>"
def acquire_job_postings(webpage_html, css_attrs: dict):
    webpage_soup = BeautifulSoup(webpage_html, "html.parser")
    jobs = [entry.string.strip() for entry in webpage_soup.find_all(attrs=css_attrs)]
    return jobs


# Filters out irrelevant job postings such as senior positions
def filter_jobs(job_list):
    # TODO: Implement this function
    raise NotImplementedError


# TODO: Acquire ALL webpages from perm storage
def acquire_webpages():
    # TODO: Implement this function
    raise NotImplementedError
