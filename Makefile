PHONY: install run virtualenv ipython clean test pflake8 fmt lint

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@python -m venv .venv

run:
	@python3 manage.py runserver


ipython:
	@.venv/bin/ipython

test:
	@python manage.py test

lint:
	@.venv/bin/pflake8 app core tests

fmt:
	@.venv/bin/isort --profile=black -m 3 app core tests
	@.venv/bin/black app core tests

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
