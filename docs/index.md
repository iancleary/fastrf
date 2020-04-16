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

## Features

- flit (virtualenv and deployment to PyPi)
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

# install all dependencies (including dev)
flit install
```

> Flit Command Line Interface documentation:
> <https://flit.readthedocs.io/en/latest/cmdline.html>

## Example Usage

```python
import fastrf

# do stuff
```

Only **Python 3.6+** is supported as required by the black, fastapi, pydantic packages

## Deploying to PyPi

Using the flit package

```bash
./scripts/deploy.sh
```
