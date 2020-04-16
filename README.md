# fastrf

<p align="center">
    <em>FastRF application, create link budgets, track key system metrics, fast to model, ready for production</em>
</p>

<p align="center">
<a href="https://travis-ci.com/iancleary/fastrf" target="_blank">
    <img src="https://travis-ci.com/iancleary/fastrf.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/iancleary/fastrf" target="_blank">
    <img src="https://codecov.io/gh/iancleary/fastrf/branch/master/graph/badge.svg" alt="Coverage">
</a>
<a href="https://codecov.io/gh/iancleary/fastrf" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/iancleary/fastrf" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastrf" target="_blank">
    <img src="https://badge.fury.io/py/fastrf.svg" alt="Package version">
</a>
<a href="https://pypi.org/project/fastrf/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastrf.svg" alt="Python Versions">
</a>
</p>

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
