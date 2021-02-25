from fastapi_camelcase import CamelModel
from pydantic import confloat

from fastrf.models.common._unit_validators import dB_unit_check_validator
from fastrf.models.signals.frequency import Frequency


class ReflectionCoefficientBase(CamelModel):
    """[Reflection Coefficient Base Model]

    Arguments:
        value {float} -- Reflection Coefficient Value, in dB
        unit {str}    -- decibels, dB
    """

    value: confloat(strict=True, le=0.0)  # type: ignore
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class ReflectionCoefficientFrequency(ReflectionCoefficientBase):
    """[Reflection Coefficient at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        value {float} -- Reflection Coefficient Value, in dB
        unit {str}    -- decibels, dB
    """

    f: Frequency


# class ReflectionCoefficientArray(CamelModel):
#     """[Reflection Coefficient vs. Frequency]

#     Arguments:
#         f {List[floats]} -- List of Frequencies, constrained to positive frequencies
#         value {List[float]} -- List of Return Loss Values
#         unit {str}    -- decibels, dB
#     """

#     f: List[confloat(strict=True, ge=0.0)]
#     values: List[confloat(strict=True, ge=0.0)]
#     unit: str = "dB"
