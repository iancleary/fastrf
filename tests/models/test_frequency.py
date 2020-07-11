import pydantic
import pytest
from fastapi_camelcase import CamelModel

from fastrf.models.signals.frequency import Frequency


def test_frequency_defaults():
    cw_signal = Frequency(value=10.0)
    assert isinstance(cw_signal, Frequency) == True


def test_frequency_class():
    cw_signal = Frequency(value=10.0)
    assert isinstance(cw_signal, CamelModel) == True


def test_negative_frequency():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        negative_frequency = Frequency(value=-10.0)


def test_improper_frequency_unit():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        frequency_with_improper_unit = Frequency(value=-10.0, unit="dHz")
