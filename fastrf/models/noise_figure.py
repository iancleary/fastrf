from pydantic import BaseModel, confloat

from ._unit_validators import dB_unit_check_validator
from .frequency import Frequency


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

    _unit_must_be_in_allowed_set = dB_unit_check_validator()


# Need to consider how to handle frequency ranges first
# class NoiseFigureArray(NoiseFigure):
#     """[Noise Figure Array vs. Frequency]

#     Arguments:
#         f {List[floats]} -- List of Frequencies, constrained to positive frequencies
#         value {List[float]} -- List of Noise Figure Values
#         unit {str}    -- decibels, dB
#     """

#     f: List[confloat(strict=True, ge=0.0)]
#     f_unit: Optional[Frequency]
#     values: List[confloat(strict=True, ge=1.0)]

#     @root_validator
#     def check_length_match(cls, values):
#         f, _values = values.get("f"), values.get("values")
#         len_f = len(f)
#         len__values = len(_values)
#         if len_f != len__values:
#             raise ValueError(
#                 f"len(f): {len_f} != len(values): {len__values}".format(
#                     len_f=len_f, len__values=len__values
#                 )
#             )
#         return values
