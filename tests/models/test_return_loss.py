import pydantic
import pytest
from fastapi_camelcase import CamelModel

from fastrf.models.interfaces.return_loss import ReturnLossBase, ReturnLossFrequency
from fastrf.models.signals.frequency import Frequency


def test_return_loss_base():
    return_loss = ReturnLossBase(value=20.0)
    assert isinstance(return_loss, ReturnLossBase) == True


def test_return_loss_base_class():
    return_loss = ReturnLossBase(value=20.0)
    assert isinstance(return_loss, CamelModel) == True


def test_return_loss_frequency():
    frequency = Frequency(value=10.0)
    return_loss = ReturnLossFrequency(f=frequency, value=20.0)
    assert isinstance(return_loss, ReturnLossFrequency) == True


def test_return_loss_improper_negative_value():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        return_loss = ReturnLossFrequency(f=frequency, value=-20.0)


def test_return_loss_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        return_loss_with_improper_value = return_loss = ReturnLossFrequency(
            f=frequency, value=2.1, unit="dBm"
        )
