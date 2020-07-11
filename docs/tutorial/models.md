# Models

[Pydantic](https://pydantic-docs.helpmanual.io/)'s `BaseModel` is used in the package to create schema that we can validate at run time for common radio-frequency (RF) models.

The purpose of these models are to capture the core concepts that comprise devices used in RF Engineering, such that these standard schemas can be used to describe parts, specifications, and their compliance from initial definition to through the complete lifecycle of the part.

## CamelCase Base Models

```python
from pydantic import BaseModel
```

is essentially equivalent to:

```python
from fastapi_camelcase import CamelModel
```

> For this tutorial, `fastapi_camelcase`'s `CamelModel` is fully backwards compatible extension of `pydantic`'s `BaseModel`!

`CamelModel` extends Pydantic's `BaseModel` by adding conversion of PEP8 variables to and from camelCase automatically!

This allows Consumers to have linters and variable names to be simultaneously compliant if they are camelCase or snake_case.

> Let the consumer decide!

If you want more information, the author has a great blog post about it: [Ahmed Nafies' "CamelCase Models with FastAPI and Pydantic"](https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee)
