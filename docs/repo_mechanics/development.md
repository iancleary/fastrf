# Development Tooling

| Tool   |      Purpose |
|---------------|:-------------|
| [Poetry](https://python-poetry.org/)  |  Dependency management, Virtual Environments, Publishing to PyPi |
| [black](https://black.readthedocs.io/en/stable/)  |  Formatting |
| [autoflake](https://github.com/myint/autoflake)  | removing unused package imports |
| [isort](https://github.com/timothycrosley/isort)  |  Dependency organization |
| [mypy](https://github.com/python/mypy)  |  Static Typing |
| [pytest](https://docs.pytest.org/en/latest/)  |  Test Coverage |
| [pre-commit](https://pre-commit.com/) | Git hook scripts to not waste time |
| [GitHub Actions](https://github.com/features/actions)  | Test and Publish (to PyPi) workflows |

## Poetry

Install Poetry on you system, and then setup a virtual environment in your fork of the repo.

```bash
poetry shell # create a virtual environment and spawn a shell in it
poetry install # install packages
```

Then run the `make` command to inspect the targets available.

```bash
make
```

Output:

```bash
(fastrf-eMJsGUfs-py3.8) ➜  fastrf git:(master) ✗ make
python-three-six:    setup python3.6 virtual environment using poetry (run poetry install afterwards)
python-three-seven:  setup python3.7 virtual environment using poetry (run poetry install afterwards)
python-three-eight:  setup python3.6 virtual environment using poetry (run poetry install afterwards)
lint:                lint the code
format:              format the code
test:                lint the code
mkdocs:              make live docs
pre-commit:          setup pre-commit hooks

> Note: the above uses the ZSH shell

```

Checkout a branch and get started with your change.

## Documentation is next

> The next page will show you how Netlify is configured to show documentation previews on all pull requests.
