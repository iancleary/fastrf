from fastapi_camelcase import CamelModel
from pydantic import confloat, root_validator
from pydantic.dataclasses import dataclass

from ..common._unit_validators import (
    ALLOWED_FREQUENCY_UNITS,
    frequency_unit_validator,
)


class Frequency(CamelModel):
    """Continuous Wave (CW) Frequency

    Args:
        value ([float]): positive frequency value
        unit ([str]): standard frequency unit for measurement, Hz, kHz, MHz, GHz, THz
    """

    value: confloat(strict=True, ge=0.0)  # Assuming negative frequencies are not needed
    unit: str = "Hz"  # SI Unit

    _unit_must_be_in_allowed_set = frequency_unit_validator()

    def get_value_in_hz(self):
        print(self.unit)
        if self.unit == "mHz":
            return self.value * 1e3
        elif self.unit == "Hz":
            return self.value
        elif self.unit == "kHz":
            return self.value / 1e3
        elif self.unit == "MHz":
            return self.value / 1e6
        elif self.unit == "GHz":
            return self.value / 1e9
        elif self.unit == "THz":
            return self.value / 1e12
        else:
            raise ValueError(
                "unit: {unit}, must be in {allowed_frequency_units}".format(
                    unit=self.unit, allowed_frequency_units=ALLOWED_FREQUENCY_UNITS
                )
            )


@dataclass
class FrequencyRange(CamelModel):
    """Model representing a range of Frequencies, starting and stopping at a range

    Args:
        start ([Frequency]): the beginning of a frequency range
        stop ([Frequency]): the end of a frequency range
    """
    def __init__(self, start: Frequency, stop: Frequency) -> None:
        pass


@dataclass
class LinearFrequencyRange(CamelModel):
    """Model representing a range of Frequencies, starting and stopping at a range

    Args:
        start ([Frequency]): the beginning of a frequency range
        stop ([Frequency]): the end of a frequency range
        step ([Frequency]): the end of a frequency range
    """
    start: Frequency
    stop: Frequency
    step: Frequency

    @root_validator
    def check_frequency_step(cls, values):
        start, stop, step = values.get('start'), values.get('stop'), values.get('step')
        print(type(start))
        number_of_steps = (
            start.get_value_in_hz() - stop.get_value_in_hz()
        ) / step.get_value_in_hz()
        print(number_of_steps)
        if isinstance(number_of_steps, int):
            return step
        else:
            raise ValueError("step is not a multiple between start and stop")
