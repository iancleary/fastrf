import pydantic
import pytest
from fastapi_camelcase import CamelModel

from fastrf.models.signals.frequency import Frequency, FrequencyRange, LinearFrequencyRange


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


def test_frequency_range():
    start = Frequency(value=10.0, unit="MHz")
    stop = Frequency(value=11.0, unit="MHz")

    frequency_range = FrequencyRange(start=start, stop=stop)
    assert isinstance(frequency_range, FrequencyRange) == True


def test_linear_frequency_range():
    start = Frequency(value=10.0, unit="GHz")
    stop = Frequency(value=20.0, unit="GHz")
    step = Frequency(value=100.0, unit="MHz")

    frequency_range = LinearFrequencyRange(start=start.dict(), stop=stop.dict(), step=step.dict())
    assert isinstance(frequency_range, LinearFrequencyRange) == True


def test_improper_step_in_linear_frequency_range():
    start = Frequency(value=10.0, unit="GHz")
    stop = Frequency(value=20.0, unit="GHz")
    step = Frequency(value=100.0, unit="GHz")

    with pytest.raises(pydantic.error_wrappers.ValidationError):
        frequency_range = LinearFrequencyRange(start=start.dict(), stop=stop.dict(), step=step.dict())
