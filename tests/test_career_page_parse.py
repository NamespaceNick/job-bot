#!/usr/bin/env python3
# test_career_page_parse.py
import jobs


def test_sucker_punch_jobs_list_titles():
    html_text = ""
    with open("sources/suckerpunch.html", "r") as src:
        html_text = src.read()

    css_val = "sc-fYxtnH leAaLw col-12 col-md-4"
    company = "Sucker Punch Productions"

    job_titles_solution = [
        "DESIGN - Narrative Writer",
        "PROGRAMMING - Senior Camera Programmer",
        "ART - Associate Outsource Artist",
        "OPS - Finance and Business Administrator",
        "PROGRAMMING - Gameplay Programmer",
        "Production - Producer",
        "ART - Senior Lighting Artist",
    ]

    job_postings = jobs.acquire_job_postings(html_text, company, css_val)

    acquired_job_titles = [jp["title"] for jp in job_postings]

    assert acquired_job_titles == job_titles_solution


def test_sucker_punch_jobs_list_basic():
    raise NotImplementedError
