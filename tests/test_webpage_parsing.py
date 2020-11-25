#!/usr/bin/env python3
# test_webpage_parsing.py
import jobs


def test_parse_class_selector_job_postings():
    html_text = ""
    with open("tests/sources/suckerpunch.html") as webpage:
        html_text = webpage.read()

    selector = ".sc-fYxtnH.leAaLw.col-12.col-md-4"
    parsed_jobs_solution = [
        "DESIGN - Narrative Writer",
        "PROGRAMMING - Senior Camera Programmer",
        "ART - Associate Outsource Artist",
        "OPS - Finance and Business Administrator",
        "PROGRAMMING - Gameplay Programmer",
        "Production - Producer",
        "ART - Senior Lighting Artist",
    ]

    assert jobs.parse_jobs_page(html_text, selector) == parsed_jobs_solution


def test_parse_relative_selector_job_postings():
    with open("tests/sources/schellgames.html") as webpage:
        html_text = webpage.read()

    selector = ".BambooHR-ATS-Jobs-Item a"
    parsed_jobs_solution = [
        "Future Internship General Submission",
        "General Submission",
        "Senior 3D Environment Artist",
        "Senior Audio Developer",
        "Technical Artist - Rigger",
        "VFX Game Artist",
        "Design Lead",
        "Senior Engineering Team Lead",
        "Associate Producer",
        "QA Associate",
    ]

    assert jobs.parse_jobs_page(html_text, selector) == parsed_jobs_solution
