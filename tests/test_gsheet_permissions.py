#!/usr/bin/env python3
# test_gsheet_permissions.py
# Tests basic gspread functionality to ensure we have proper permissions for
# the Google Sheet
import jobs

TEST_WORKSHEET_NAME = "TEST (IGNORE)"


def test_read_placeholder_cells():
    placeholder_row_solution = ["spam", "ham", "eggs"]

    worksheet = jobs.spreadsheet.worksheet(TEST_WORKSHEET_NAME)
    placeholder_row = worksheet.row_values(1)

    assert placeholder_row == placeholder_row_solution


def test_write_placeholder_cells():
    worksheet = jobs.spreadsheet.worksheet(TEST_WORKSHEET_NAME)

    worksheet.update("B2", "foobar")
    assert worksheet.acell("B2").value == "foobar"

    worksheet.update("B2", "")
    assert worksheet.acell("B2").value == ""
