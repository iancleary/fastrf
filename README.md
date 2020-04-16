# fastrf

[![Build Status](https://img.shields.io/travis/com/iancleary/fastrf/master.svg)](https://img.shields.io/travis/com/iancleary/fastrf)
[![image](https://img.shields.io/pypi/v/fastrf.svg)](https://pypi.org/project/fastrf/)
[![Updates](https://pyup.io/repos/github/iancleary/fastrf/shield.svg)](https://pyup.io/repos/github/iancleary/fastrf/)
[![image](https://img.shields.io/pypi/l/fastrf.svg)](https://pypi.org/project/fastrf/)
[![image](https://img.shields.io/pypi/pyversions/fastrf.svg)](https://pypi.org/project/fastrf/)
[![image](https://img.shields.io/github/contributors/iancleary/fastrf.svg)](https://github.com/iancleary/fastrf/graphs/contributors)

## The Basic Idea

Fastrf is a web server that makes it easy to create radio frequency (RF) gain line ups 📡, link budgets 🌎📡🛰️, and simulation models 🧪🧮 to caputre the performance of a RF system.

This project will stand on the shoulders of some giants:
- [https://github.com/tiangolo/fastapi/](https://github.com/tiangolo/fastapi/)
- [https://github.com/samuelcolvin/pydantic/](https://github.com/samuelcolvin/pydantic/)
- [https://github.com/scikit-rf/scikit-rf](https://github.com/scikit-rf/scikit-rf)

## Features

- flit (virtualenv and deployment to PyPi)
- black (linting/formatter)
- autoflake (removing unused packages)
- isort (dependency organization)
- mypy (static type checking)
- pytest (including test coverage)
- travis-ci for CI/CD

## Documentation

Documentation is hosted at[fastrf.iancleary.me](https://fastrf.iancleary.me/).

> Thank you to Netlify for builds and hosts the documentation 🙂🚀🎉!

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

## Requirements.txt and runtime.txt

This allows Netlify to build the docs, and is not for fastrf developmen.

These are required to configure Netlify's deployment and pull request previews for mkdocs

### Requirements.txt

<https://docs.netlify.com/configure-builds/common-configurations/#mkdocs>

#### Runtime.txt

Specifies python version for Netlify

<https://docs.netlify.com/configure-builds/manage-dependencies/#python>

## Deploying to PyPi

Using the flit package

```bash
./scripts/deploy.sh
```
