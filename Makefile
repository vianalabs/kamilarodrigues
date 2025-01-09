PHONY: install run virtualenv ipython clean test pflake8 fmt lint

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@python -m venv .venv

run:
	@python manage.py runserver


ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -vs -s

lint:
	@.venv/bin/pflake8 app core

fmt:
	@.venv/bin/isort --profile=black -m 3 app core
	@.venv/bin/black app core

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
