import pydantic
import pytest
from fastapi_camelcase import CamelModel

from fastrf.models.interfaces.reflection_coefficient import (
    ReflectionCoefficientBase,
    ReflectionCoefficientFrequency,
)
from fastrf.models.signals.frequency import Frequency


def test_reflection_coefficient_base():
    reflection_coefficient = ReflectionCoefficientBase(value=-20.0)
    assert isinstance(reflection_coefficient, ReflectionCoefficientBase) == True


def test_reflection_coefficient_base_class():
    return_loss = ReflectionCoefficientBase(value=-20.0)
    assert isinstance(return_loss, CamelModel) == True


def test_reflection_coefficient_frequency():
    frequency = Frequency(value=10.0)
    reflection_coefficient = ReflectionCoefficientFrequency(f=frequency, value=-20.0)
    assert isinstance(reflection_coefficient, ReflectionCoefficientFrequency) == True


def test_reflection_coefficient_improper_positive_value():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        reflection_coefficient = ReflectionCoefficientFrequency(f=frequency, value=20.0)


def test_reflection_coefficient_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        reflection_coefficient_with_improper_value = ReflectionCoefficientFrequency(
            f=frequency, value=-30.0, unit="dBm"
        )
