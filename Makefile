.PHONY: help

# Shell that make should use
SHELL:=bash

# Capture git branch and hash information
# https://stackoverflow.com/questions/43008842/capture-git-branch-name-in-makefile-variable
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
HASH := $(shell git rev-parse HEAD)

# - to suppress if it doesn't exist
-include make.env

help:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# adds anything that has a double # comment to the phony help list
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ".:*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint: ## lint the code
lint:
	bash scripts/lint.sh

format: ## format the code
format:
	bash scripts/format.sh

test: ## lint the code
test:
	bash scripts/test.sh

docs-live: ## make live docs
docs-live:
	bash scripts/docs-live.sh

install: ## uninstall and install package with python
install:
	echo y | pip uninstall fastrf
	python setup.py build
	python setup.py install

install-editable: ## uninstall and install package with python, editable
install-editable:
	# https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
	echo y | pip uninstall fastrf
	python setup.py build
	python setup.py develop
	# python -m pip install -e .

develop:
develop: ## Setups a Python3 (latest) development environment pipenv and flit
	make develop-three-eight

develop-three-eight:  ## Setups a Python3.8 development environment pipenv and flit
develop-three-eight:
	# https://flit.readthedocs.io/en/latest/cmdline.html
	pipenv --python 3.8
	pipenv run python3 -m pip install flit
	pipenv run flit install
	pipenv shell

develop-three-seven:  ## Setups a python3.7 development environment pipenv and flit
develop-three-seven:
	# https://flit.readthedocs.io/en/latest/cmdline.html
	pipenv --python 3.7
	pipenv run python3 -m pip install flit
	pipenv run flit install
	pipenv shell

develop-three-six:  ## Setups a python3.7 development environment pipenv and flit
develop-three-six:
	# https://flit.readthedocs.io/en/latest/cmdline.html
	pipenv --python 3.6
	pipenv run python3 -m pip install flit
	pipenv run flit install
	pipenv shell

clean:
clean: ## exists pipenv, cleans virtual environment
	-pipenv --rm
	rm -rf dist/
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm .coverage
	rm Pipfile
