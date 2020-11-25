DIFF ?= false
default:
	- python jobs.py

init:
	pip install -r requirements.txt

test: run_tests clean
	
# Show diff if DIFF variable is defined
ifeq ($(DIFF),true)
run_tests:
	- python -m pytest -vv tests
else
run_tests:
	- python -m pytest tests
endif

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache
