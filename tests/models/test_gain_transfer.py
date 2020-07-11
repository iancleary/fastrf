import pydantic
import pytest

from fastrf.models.gain_transfer import (
    Gain,
    GainBase,
    GainTransferBase,
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
    assert isinstance(gain_transfer, GainBase) == True


def test_gain():
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = Gain(value=60.0, input_power=input_power, output_power=output_power)
    assert isinstance(gain_transfer, Gain) == True


def test_gain_transfer_base():
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = GainTransferBase(input_power=input_power, output_power=output_power)
    assert isinstance(gain_transfer, GainTransferBase) == True


def test_gain_transfer_frequency():
    frequency = Frequency(value=10.0)
    input_power = Power(value=-50.0)
    output_power = Power(value=10.0)
    gain_transfer = GainTransferFrequency(
        f=frequency, input_power=input_power, output_power=output_power
    )
    assert isinstance(gain_transfer, GainTransferFrequency) == True


def test_gain_transfer_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        gain_transfer_with_improper_value = GainTransferBase(
            f=frequency, value=2.1, unit="dBm"
        )
