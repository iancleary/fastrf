from fastapi_camelcase import CamelModel
from pydantic import confloat

from fastrf.models.common._unit_validators import frequency_unit_validator


class Frequency(CamelModel):
    value: confloat(strict=True, ge=0.0)  # type: ignore
    # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()


# How should ranges, channels and bands relate?  Inspiration for skrf?


# class FrequencyRange(CamelModel):
#     start: Frequency
#     stop: Frequency
#     step: Frequency
