from pydantic import BaseModel, confloat

from ..common._unit_validators import dB_unit_check_validator
from ..signals.frequency import Frequency


class ReturnLossBase(BaseModel):
    """[Return Loss Base Model]

    Arguments:
        value {float} -- Return Loss Value, in dB
        unit {str}    -- decibels, dB
    """

    value: confloat(strict=True, ge=0.0)
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class ReturnLossFrequency(ReturnLossBase):
    """[Return Loss at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        value {float} -- Return Loss Value, in dB
        unit {str}    -- decibels, dB
    """

    f: Frequency


# class ReturnLossArray(BaseModel):
#     """[Return Loss vs. Frequency]

#     Arguments:
#         f {List[floats]} -- List of Frequencies, constrained to positive frequencies
#         value {List[float]} -- List of Return Loss Values
#         unit {str}    -- decibels, dB
#     """

#     f: List[confloat(strict=True, ge=0.0)]
#     values: List[confloat(strict=True, ge=0.0)]
#     unit: str = "dB"