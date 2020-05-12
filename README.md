# fastrf

<p align="center">
    <em>FastRF application, create link budgets, track key system metrics, fast to model, ready for production</em>
</p>

<p align="center">
<a href="https://github.com/iancleary/fastrf/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/iancleary/fastrf/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/iancleary/fastrf/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/iancleary/fastrf/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://codecov.io/gh/iancleary/fastrf" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/iancleary/fastrf?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastrf" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastrf?color=%2334D058&label=pypi%20package" alt="Package version">
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

- Poetry (virtualenv and deployment to PyPi)
- black (linting/formatter)
- autoflake (removing unused packages)
- isort (dependency organization)
- mypy (static type checking)
- pytest (including test coverage)
- GitHub Actions for CI/CD

## Documentation

Documentation is hosted at [fastrf.iancleary.me](https://fastrf.iancleary.me/).

> Thank you to Netlify for builds and hosts the documentation 🙂🚀🎉!

### Netlify and Mkdocs

The `requirements.txt` and `runtime.txt` enable Netlify to build the docs.

> They are not for fastrf development. pyproject.toml specifies poetry's settings

These are required to configure Netlify's deployment and pull request previews for mkdocs

#### Requirements.txt

<https://docs.netlify.com/configure-builds/common-configurations/#mkdocs>

#### Runtime.txt

Specifies python version for Netlify

<https://docs.netlify.com/configure-builds/manage-dependencies/#python>

## Installing fastrf

Install the latest release:

```bash
pip install fastrf
```

Or you can clone `fastrf` and get started locally

```bash
# install all dependencies (including dev)
make python-three-six
```

### Dependencies

The `pyproject.toml` file is used by [poetry](https://python-poetry.org/) to install dependencies into a virtual environment.

> Poetry Command Line Interface Documnetation:
> <https://python-poetry.org/docs/cli/>

## Example Usage

```python
import fastrf

# do stuff
```

Only **Python 3.6+** is supported as required by the black, fastapi, pydantic packages
