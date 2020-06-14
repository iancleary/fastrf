from pydantic import BaseModel, confloat

from ..common._unit_validators import frequency_unit_validator


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()


# How should ranges, channels and bands relate?  Inspiration for skrf?


# class FrequencyRange(BaseModel):
#     start: Frequency
#     stop: Frequency
#     step: Frequency
