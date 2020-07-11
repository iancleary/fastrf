from typing import Optional

from fastapi_camelcase import CamelModel

from .common._unit_validators import dB_unit_check_validator, power_unit_validator
from .signals.frequency import Frequency


class Power(CamelModel):
    value: float
    unit: str = "dBm"

    _unit_must_be_in_allowed_set = power_unit_validator()


class GainBase(CamelModel):
    value: float
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class Gain(GainBase):
    input_power: Optional[Power]
    output_power: Optional[Power]


class GainTransferBase(CamelModel):
    """[Input Power vs. Output Power Base Model]

    Arguments:
        input_power {Power} -- Input power in dBm
        output_power {Power} -- Output power in dBm
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB
    """

    input_power: Power
    output_power: Power
    gain: Optional[Gain]
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class GainTransferFrequency(CamelModel):
    """[Input Power vs. Output Power at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        input_power {Power} -- Input power in dBm
        output_power {Power} -- Output power in dBm
        value {float} -- Noise Figure Value, in dB
        unit {str}    -- decibels, dB

    """

    f: Frequency
