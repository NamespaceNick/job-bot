#!/usr/bin/env python3
# test_gsheet_acquire_webpages.py
import jobs


# TODO: Move to test spreadsheet to ensure test-data doesn't change
def test_acquire_single_company_page_info():
    company_info_solutions = [
        {
            "company": "Sucker Punch Productions",
            "url": "jobs.suckerpunch.com",
            "attribute": "class",
            "attr_val": "sc-fYxtnH leAaLw col-12 col-md-4",
        },
        {
            "company": "Naughty Dog",
            "url": "naughtydog.com/careers",
            "attribute": "class",
            "attr_val": "d-block link-off-white",
        },
    ]

    first_two_companies_info = jobs.acquire_webpages()[:2]

    assert first_two_companies_info == company_info_solutions
