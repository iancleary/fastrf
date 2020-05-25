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


# How should ranges, channels and bands relate?  Inspiration for skrf?


# class FrequencyRange(BaseModel):
#     start: Frequency
#     stop: Frequency
#     step: Frequency
