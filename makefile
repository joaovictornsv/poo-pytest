create-venv:
	rm -rf .venv && python3 -m venv .venv;

pip-requirements:
	pip3 install -r requirements.txt;


pip-freeze:
	pip freeze > requirements.txt

flake8:
	python3 -m flake8 ./src

test:
	pytest

test-coverage:
	pytest --cov=src --cov-report html:coverage --cov-config=.coveragerc --cov-fail-under=90
