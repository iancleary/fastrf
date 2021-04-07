import pydantic
import pytest
from fastapi_camelcase import CamelModel

from fastrf.models.gain_transfer import (
    Gain,
    GainFrequency,
    GainTransfer,
    GainTransferFrequency,
    Power,
)
from fastrf.models.signals.frequency import Frequency


def test_power():
    power = Power(value=-50.0)
    assert isinstance(power, Power) == True


def test_power_improper_unit():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        power = Power(value=-50.0, unit="dB")


def test_gain_base():
    gain_transfer = Gain(value=60.0)
    assert isinstance(gain_transfer, Gain) == True


def test_gain_base_class():
    gain_transfer = Gain(value=60.0)
    assert isinstance(gain_transfer, CamelModel) == True


def test_gain_frequency():
    gain_transfer = GainFrequency(value=60.0, f=Frequency(value=15.0e9))
    assert isinstance(gain_transfer, GainFrequency) == True


def test_gain_transfer_base():
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = GainTransfer(input_power=input_power, output_power=output_power)
    assert isinstance(gain_transfer, GainTransfer) == True


def test_gain_transfer_frequency():
    frequency = Frequency(value=10.0e9)
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = GainTransferFrequency(
        f=frequency, input_power=input_power, output_power=output_power
    )
    assert isinstance(gain_transfer, GainTransferFrequency) == True


def test_gain_transfer_improper_unit():
    frequency = Frequency(value=10.0e9)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        gain_transfer_with_improper_value = GainTransfer(
            f=frequency, value=2.1, unit="dBm"
        )
