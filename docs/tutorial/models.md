# Models

[Pydantic](https://pydantic-docs.helpmanual.io/)'s `BaseModel` is used in the package to create schema that we can validate at run time for common radio-frequency (RF) models.

The purpose of these models are to capture the core concepts that comprise devices used in RF Engineering, such that these standard schemas can be used to describe parts, specifications, and their compliance from initial definition to through the complete lifecycle of the part.

## Walkthrough

**Let's start with the common attributes**, like frequency, noise figure, gain, and return loss (and reflection coefficient).

## Frequency

There is a little to unpack here, so let's walk through it

```python
from pydantic import BaseModel, confloat, validator


def frequency_unit_check(unit: str) -> None:
    allowed_frequency_units = {"mHz", "Hz", "Khz", "MHz", "GHz", "THz"}
    if unit not in allowed_frequency_units:
        raise ValueError(
            "unit: {unit}, must be in {allowed_frequency_units}".format(
                unit=unit, allowed_frequency_units=allowed_frequency_units
            )
        )


def frequency_unit_validator():
    return validator("unit", allow_reuse=True)(frequency_unit_check)


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()
```

First off, `confloat` is a `float` type with extra validation.  In this case, it is required to have positive frequency greater than 0.0 Hz.

We import `validator` from `pydantic` to be able to re-use the frequency unit validator multiple places. I'm still working through how to link frequencies between a frequency instance and, say, a noise figure specification.

> Links as relationships in a database schema are the thought here

*Reference: <https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf>*
