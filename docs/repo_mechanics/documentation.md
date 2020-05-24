# Documentation

Documentation is hosted at [fastrf.iancleary.me](https://fastrf.iancleary.me/).

> Thank you to Netlify for builds and hosts the documentation 🙂🚀🎉!

## Netlify and Mkdocs

The `requirements.txt` and `runtime.txt` enable Netlify to build the docs.

> They are not for fastrf development. pyproject.toml specifies poetry's settings

These are required to configure Netlify's deployment and pull request previews for mkdocs

## Requirements.txt

<https://docs.netlify.com/configure-builds/common-configurations/#mkdocs>

## Runtime.txt

Specifies python version for Netlify

<https://docs.netlify.com/configure-builds/manage-dependencies/#python>

## Local changes

Run the make command at the root level of the repo.

```bash
make
```

Output:

```bash
(fastrf-eMJsGUfs-py3.8) ➜  fastrf git:(master) ✗ make
...
mkdocs:                        make live docs
```

## Pull Request Previews

Netlify is configured to create a previews on every pull request, so we can discuss your changes there
