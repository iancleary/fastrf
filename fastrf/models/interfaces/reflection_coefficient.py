from pydantic import BaseModel, confloat

from ..common._unit_validators import dB_unit_check_validator
from ..common.frequency import Frequency


class ReflectionCoefficient(BaseModel):
    """[Reflection Coefficient at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        value {float} -- Reflection Coefficient Value, in dB
        unit {str}    -- decibels, dB
    """

    f: Frequency
    value: confloat(strict=True, le=0.0)
    unit: str = "dB"

    _unit_must_be_in_allowed_set = dB_unit_check_validator()


# class ReflectionCoefficientArray(BaseModel):
#     """[Reflection Coefficient vs. Frequency]

#     Arguments:
#         f {List[floats]} -- List of Frequencies, constrained to positive frequencies
#         value {List[float]} -- List of Return Loss Values
#         unit {str}    -- decibels, dB
#     """

#     f: List[confloat(strict=True, ge=0.0)]
#     values: List[confloat(strict=True, ge=0.0)]
#     unit: str = "dB"
