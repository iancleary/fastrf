import pydantic
import pytest
from fastrf.models.common.frequency import Frequency
from fastrf.models.interfaces.return_loss import ReturnLoss


def test_return_loss_defaults():
    frequency = Frequency(value=10.0)
    return_loss = ReturnLoss(f=frequency, value=20.0)
    assert isinstance(return_loss, ReturnLoss) == True


def test_return_loss_improper_negative_value():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        return_loss = ReturnLoss(f=frequency, value=-20.0)


def test_return_loss_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        return_loss_with_improper_value = return_loss = ReturnLoss(
            f=frequency, value=2.1, unit="dBm"
        )
