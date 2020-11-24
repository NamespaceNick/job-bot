#!/usr/bin/env python3
# test_career_page_parse.py
import jobs


def test_sucker_punch_jobs_list_titles():
    html_text = ""
    with open("tests/sources/suckerpunch.html", "r") as src:
        html_text = src.read()

    css_attrs = {"class": "sc-fYxtnH leAaLw col-12 col-md-4"}

    job_titles_solution = [
        "DESIGN - Narrative Writer",
        "PROGRAMMING - Senior Camera Programmer",
        "ART - Associate Outsource Artist",
        "OPS - Finance and Business Administrator",
        "PROGRAMMING - Gameplay Programmer",
        "Production - Producer",
        "ART - Senior Lighting Artist",
    ]

    job_postings = jobs.acquire_job_postings(html_text, css_attrs)

    assert job_postings == job_titles_solution


def test_sucker_punch_jobs_list_basic():
    raise NotImplementedError
