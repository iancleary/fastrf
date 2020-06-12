# Models

[Pydantic](https://pydantic-docs.helpmanual.io/)'s `BaseModel` is used in the package to create schema that we can validate at run time for common radio-frequency (RF) models.

The purpose of these models are to capture the core concepts that comprise devices used in RF Engineering, such that these standard schemas can be used to describe parts, specifications, and their compliance from initial definition to through the complete lifecycle of the part.

## Walkthrough

**Let's start with the common attributes**, like frequency, noise figure, gain transfer, and return loss (and reflection coefficient).

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

`unit` is a common attribute for any `fastrf` model that will always be a string representing the common unit.  It is not required to be the scientific unit (only Hz and not kHz, MHz, etc. for Frequency).

This is primarily to bind `unit` to the model, so that it is not scattered throughout your code.

### Confloat

`confloat` is a `float` type with extra validation.  In this case, it is required to have positive frequency greater than 0.0 Hz.

### Validator

We import `validator` from `pydantic` to be able to re-use the frequency unit validator multiple places.

### Linking models

I'm still working through how to link frequencies between a frequency instance and, say, a noise figure specification.

> Links as relationships in a database schema are the thought here

*Reference: <https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf>*

## Noise Figure

From `pydantic`, we've seen `BaseModel` and `confloat` in the Frequency model.

Additionally, the `unit` attribute is used here as well.

```python
from pydantic import BaseModel, confloat

from .common._unit_validators import dB_unit_check_validator
from .signals.frequency import Frequency


class NoiseFigure(BaseModel):
    """[Noise Figure at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB
    """

    f: Frequency
    value: confloat(strict=True, ge=1.0)
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()
```

Noise figure must be positive and greater than 1.0 dB.

The unit validator here enforces that the unit is "dB" and will be used in other models as well.

> Note that this is a model for a specification or measured value.  We are making an assumption that near perfect noise figure and measurement error doesn't result in an erroneous value < 1.0 dB.

## Gain Transfer

At a given input power, gain transfer is the measure of how much forward gain a two port device has.

First we define a model for Power:

```Python hl_lines="3 4 5"
from pydantic import BaseModel

class Power(BaseModel):
    value: float
    unit: str = "dBm"

```

Next, we set up a model for an input and output power

```Python hl_lines="9 10 11  13 23 24"
from typing import Optional

from pydantic import BaseModel

from .common._unit_validators import dB_unit_check_validator
from .signals.frequency import Frequency


class Power(BaseModel):
    value: float
    unit: str = "dBm"

class GainTransfer(BaseModel):
    """[Input Power vs. Output Power at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB
    """

    f: Frequency
    input_power: Power
    output_power: Power
    gain: Optional[float]
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()
```
