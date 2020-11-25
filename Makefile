DIFF ?= false
default:
	- python jobs.py

init:
	pip install -r requirements.txt

test: run_tests clean

test-diff: run_diff_tests clean
	
run_tests:
	- python -m pytest tests

run_diff_tests:
	- python -m pytest -vv tests

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache
