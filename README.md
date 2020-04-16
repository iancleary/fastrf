# fastrf

[![Build Status](https://img.shields.io/travis/com/iancleary/fastrf/master.svg)](https://img.shields.io/travis/com/iancleary/fastrf)
[![image](https://img.shields.io/pypi/v/fastrf.svg)](https://pypi.org/project/fastrf/)
[![Updates](https://pyup.io/repos/github/iancleary/fastrf/shield.svg)](https://pyup.io/repos/github/iancleary/fastrf/)
[![image](https://img.shields.io/pypi/l/fastrf.svg)](https://pypi.org/project/fastrf/)
[![image](https://img.shields.io/pypi/pyversions/fastrf.svg)](https://pypi.org/project/fastrf/)
[![image](https://img.shields.io/github/contributors/iancleary/fastrf.svg)](https://github.com/iancleary/fastrf/graphs/contributors)

## The Basic Idea

This is a template module collecting many utilities I have liked from other projects, to serve as a personal reference.
- [https://github.com/tiangolo/fastapi/](https://github.com/tiangolo/fastapi/)
- [https://github.com/cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter)

## Features

- pipenv (sane virtualenv)
- black (linting/formatter)
- autoflake (removing unused packages)
- isort (dependency organization)
- mypy (static type checking)
- pytest (including test coverage)
- travis-ci for CI/CD

## Installing fastrf

Install the latest release:

```bash
pip install fastrf
```

Or you can clone `fastrf` and get started locally

```bash

# ensure you have pipenv installed
pip install --user pipenv

# install all dependencies (including dev)
pipenv install --dev

# start a shell in pipenv
pipenv shell

# develop!

```

## Example Usage

```python
import fastrf

# do stuff
```

Only **Python 3.6+** is supported as required by the black, pydantic packages

## Deploying to PyPi

Using the flit package

```bash
./scripts/deploy.sh
# TBD detail about flit setup
```
