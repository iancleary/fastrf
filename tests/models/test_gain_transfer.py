import pydantic
import pytest
from fastrf.models.gain_transfer import GainTransfer, Power
from fastrf.models.signals.frequency import Frequency


def test_gain_transfer_defaults():
    frequency = Frequency(value=10.0)
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = GainTransfer(
        f=frequency, input_power=input_power, output_power=output_power
    )
    assert isinstance(gain_transfer, GainTransfer) == True


def test_gain_transfer_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        gain_transfer_with_improper_value = GainTransfer(
            f=frequency, value=2.1, unit="dBm"
        )
