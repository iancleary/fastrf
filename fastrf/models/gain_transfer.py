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
