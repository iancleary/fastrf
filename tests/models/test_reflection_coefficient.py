import pydantic
import pytest
from fastrf.models.common.frequency import Frequency
from fastrf.models.interfaces.reflection_coefficient import ReflectionCoefficient


def test_reflection_coefficient_defaults():
    frequency = Frequency(value=10.0)
    reflection_coefficient = ReflectionCoefficient(f=frequency, value=-20.0)
    assert isinstance(reflection_coefficient, ReflectionCoefficient) == True


def test_reflection_coefficient_improper_positive_value():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        reflection_coefficient = ReflectionCoefficient(f=frequency, value=20.0)


def test_reflection_coefficient_improper_unit():
    frequency = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        reflection_coefficient_with_improper_value = ReflectionCoefficient(
            f=frequency, value=-30.0, unit="dBm"
        )
