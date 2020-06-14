# Models

[Pydantic](https://pydantic-docs.helpmanual.io/)'s `BaseModel` is used in the package to create schema that we can validate at run time for common radio-frequency (RF) models.

The purpose of these models are to capture the core concepts that comprise devices used in RF Engineering, such that these standard schemas can be used to describe parts, specifications, and their compliance from initial definition to through the complete lifecycle of the part.

## Walkthrough

**Let's start with the common attributes**, like frequency, noise figure, gain transfer, and return loss (and reflection coefficient).

## Frequency

There is a little to unpack here, so let's walk through it

```Python hl_lines="6"
from pydantic import BaseModel, confloat

from ..common._unit_validators import frequency_unit_validator


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()

```

`unit` is a common attribute for any `fastrf` model that will always be a string representing the common unit.

### Positive Frequencies

`confloat` is a `float` type with extra validation.  In this case, it is required to have positive frequency greater than 0.0 Hz.

```Python hl_lines="7"
from pydantic import BaseModel, confloat

from ..common._unit_validators import frequency_unit_validator


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()

```

### Allowed units

Notice that the unit is not required to be the scientific unit (only Hz and not kHz, MHz, etc. for Frequency).

```Python hl_lines="8 9 10"
from pydantic import BaseModel, confloat

from ..common._unit_validators import frequency_unit_validator


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()

```

This is primarily to bind `unit` to the model, so that it is not scattered throughout your code.

> How does this work?

#### Re-usable validators

Pydantic has a concept of re-usable validators.

The `fastrf.models.common._unit_validators.py` module is where common RF validators are located.

We import `validator` from `pydantic` to be able to re-use the frequency unit validator multiple places.

```Python hl_lines=" 1 6"
from pydantic import validator

...

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
```

### Linking models

I'm still working through how to link frequencies between a frequency instance and, say, a noise figure specification.

> Links as relationships in a database schema are the thought here

*Reference: <https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf>*

## Noise Figure

From `pydantic`, we've seen `BaseModel` and `confloat` in the Frequency model.

> **Unit validation is seen here as well!**

```python hl_lines="3 12 16 18"
from pydantic import BaseModel, confloat

from .common._unit_validators import dB_unit_check_validator
from .signals.frequency import Frequency


class NoiseFigureBase(BaseModel):
    """[Noise Figure Base Model]

    Arguments:
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB
    """

    value: confloat(strict=True, ge=1.0)
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()
```

> **Noise figure must be positive and greater than 1.0 dB.**

```python hl_lines="3 11"
...

class NoiseFigureBase(BaseModel):
    """[Noise Figure Base Model]

    Arguments:
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB
    """

    value: confloat(strict=True, ge=1.0)

...
```

> Note that this is a model for a specification or measured value.  We are making an assumption that near perfect noise figure and measurement error doesn't result in an erroneous value < 1.0 dB.

-----------------------------

Let's continue with defining several models:

* Power
* GainBase
* Gain (with input and output power)

## Power

First we define a model for Power:

> **Unit validation is seen here as well!**

```Python hl_lines="6 10"
from pydantic import BaseModel

from .common._unit_validators import power_unit_validator


class Power(BaseModel):
    value: float
    unit: str = "dBm"

    _unit_must_be_in_allowed_set = power_unit_validator()

```

Tell me if you see a pattern 😊

-----------------------------

## Gain

Let's continue to Gain! 🎉

```Python hl_lines="10 16 23"
from typing import Optional

from pydantic import BaseModel

from .common._unit_validators import dB_unit_check_validator, power_unit_validator
from .signals.frequency import Frequency

...

class GainBase(BaseModel):
    value: float
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class Gain(GainBase):
    input_power: Optional[Power]
    output_power: Optional[Power]
```

> We use the `Power` model to classify if the Gain value's operating points.

-----------------------------

## Gain Transfer

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

-----------------------------


Now that we have a sense for the common `Pydantic` models, let's talk about development tooling in the repo!
