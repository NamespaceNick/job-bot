#!/usr/bin/env python3
# test_filter_jobs.py
import jobs


def test_all_jobs_filtered_out():
    all_senior_jobs = [
        "Senior Gameplay Engineer",
        "Senior 3D Artist",
        "Executive Producer",
        "Art Director",
        "Production Director",
        "Lead Combat Designer",
    ]

    assert jobs.filter_jobs(all_senior_jobs) == []
