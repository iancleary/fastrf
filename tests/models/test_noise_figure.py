import pydantic
import pytest
from fastrf.models.noise_figure import NoiseFigureBase, NoiseFigureFrequency
from fastrf.models.signals.frequency import Frequency


def test_noise_figure_base():
    noise_figure = NoiseFigureBase(value=2.1)
    assert isinstance(noise_figure, NoiseFigureBase) == True


def test_noise_figure_at_frequency_defaults():
    cw_signal = Frequency(value=10.0)
    noise_figure = NoiseFigureFrequency(f=cw_signal, value=2.1)
    assert isinstance(noise_figure, NoiseFigureFrequency) == True


def test_noise_figure_improper_negative_value():
    cw_signal = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        noise_figure_with_improper_value = noise_figure = NoiseFigureBase(
            f=cw_signal, value=-3.0
        )


def test_noise_figure_improper_unit():
    cw_signal = Frequency(value=10.0)
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        noise_figure_with_improper_value = noise_figure = NoiseFigureBase(
            f=cw_signal, value=2.1, unit="dBm"
        )


# def test_noise_figure_array_defaults():
#     cw_signal = Frequency(value=10.0)
#     with pytest.raises(pydantic.error_wrappers.ValidationError):
#         noise_figure_with_improper_value = noise_figure = NoiseFigure(
#             f=cw_signal, value=2.1, unit="dBm"
#         )


# def test_noise_figure_array_length_mismatch():
#     freqencies = [1.0, ]
#     with pytest.raises(pydantic.error_wrappers.ValidationError):
#         noise_figure_with_improper_value = noise_figure = NoiseFigure(
#             f=cw_signal, value=2.1, unit="dBm"
#         )
