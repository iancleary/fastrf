from pydantic import BaseModel, confloat, validator


class Frequency(BaseModel):
    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    @validator("unit")
    def unit_must_be_in_allowed_set(cls, v):
        allowed_frequency_units = {"mHz", "Hz", "Khz", "MHz", "GHz", "THz"}
        if v not in allowed_frequency_units:
            raise ValueError(
                "unit: {v}, must be in {allowed_frequency_units}".format(
                    v=v, allowed_frequency_units=allowed_frequency_units
                )
            )

# How should ranges, channels and bands relate?  Inspiration for skrf?


# class FrequencyRange(BaseModel):
#     start: Frequency
#     stop: Frequency
#     step: Frequency
