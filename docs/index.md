# fastrf

<p align="center">
    <em>FastRF application, create link budgets, track key system metrics, fast to model, ready for production</em>
</p>

<p align="center">

<a href="https://app.netlify.com/sites/fastrf/deploys" target="_blank">
    <img src="https://api.netlify.com/api/v1/badges/3c2a6494-9acb-40ce-b23e-da29a2d0bd91/deploy-status" alt="Netlify Status">
<a href="https://github.com/iancleary/fastrf/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/iancleary/fastrf/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/iancleary/fastrf/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/iancleary/fastrf/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://dependabot.com/" target="_blank">
    <img src="https://flat.badgen.net/dependabot/iancleary/fastrf?icon=dependabot" alt="Dependabot Enabled">
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

## Installing fastrf

Install the latest release:

```bash
pip install fastrf
```

## Documentation

Documentation is hosted at [fastrf.iancleary.me](https://fastrf.iancleary.me/).

## Dependencies

The `pyproject.toml` file is used by [poetry](https://python-poetry.org/) to install dependencies into a virtual environment.

> Poetry Command Line Interface Documnetation:
> <https://python-poetry.org/docs/cli/>

Only **Python 3.6+** is supported as required by the black, fastapi, pydantic packages
