from typing import Optional

from fastapi_camelcase import CamelModel

from .common._unit_validators import dB_unit_check_validator, power_unit_validator
from .signals.frequency import Frequency


class Power(CamelModel):
    value: float
    unit: str = "dBm"

    _unit_must_be_in_allowed_set = power_unit_validator()


class Gain(CamelModel):
    value: float
    unit: str = "dB"

    _unit_must_be_dB = dB_unit_check_validator()


class GainFrequency(Gain):
    """[Gain at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        gain {Gain} -- Gain in dB
    """

    f: Frequency


class GainTransfer(CamelModel):
    """[Input Power vs. Output Power Base Model]

    Arguments:
        input_power {Power} -- Input power in dBm
        output_power {Power} -- Output power in dBm
    """

    input_power: Power
    output_power: Power
    gain: Optional[Gain]


class GainTransferFrequency(GainTransfer):
    """[Input Power vs. Output Power at a single frequency]

    Arguments:
        f {Frequency} -- Single Frequency
        input_power {Power} -- Input power in dBm
        output_power {Power} -- Output power in dBm

    """

    f: Frequency
