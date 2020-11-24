default:
	- python jobs.py

init:
	pip install -r requirements.txt

test: run_tests clean
	
run_tests:
	- python -m pytest tests

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache
