from pydantic import validator


def dB_unit_check(unit: str) -> None:
    if unit != "dB":
        raise ValueError("unit: {unit}, must be dB".format(unit=unit))


def dB_unit_check_validator():
    return validator("unit", allow_reuse=True)(dB_unit_check)


def power_unit_check(unit: str) -> None:
    allowed_power_units = {"W", "dBm", "dBW"}
    if unit not in allowed_power_units:
        raise ValueError(
            "unit: {unit}, must be in {allowed_power_units}".format(
                unit=unit, allowed_power_units=allowed_power_units
            )
        )


def power_unit_validator():
    return validator("unit", allow_reuse=True)(power_unit_check)


ALLOWED_FREQUENCY_UNITS = {"mHz", "Hz", "Khz", "MHz", "GHz", "THz"}


def frequency_unit_check(unit: str) -> None:
    if unit not in ALLOWED_FREQUENCY_UNITS:
        raise ValueError(
            "unit: {unit}, must be in {allowed_frequency_units}".format(
                unit=unit, allowed_frequency_units=ALLOWED_FREQUENCY_UNITS
            )
        )


def frequency_unit_validator():
    return validator("unit", allow_reuse=True)(frequency_unit_check)


# def frequency_step_check(cls, values):
#     start, stop, step = values.get('start'), values.get('stop'), values.get('step')

#     number_of_steps = (
#         start.get_value_in_hz() - stop.get_value_in_hz()
#     ) / step.get_value_in_hz()
#     print(number_of_steps)
#     if isinstance(number_of_steps, int):
#         return step
#     else:
#         raise ValueError("step is not a multiple between start and stop")


# def frequency_step_validator():
#     return root_validator("step", allow_reuse=True)(frequency_step_check)


# ----------------------------------------------------------------------


# def dBc_unit_check(unit: str) -> None:
#     if unit != "dBc":
#         raise ValueError("unit: {unit}, must be dBc".format(unit=unit))


# def dBc_unit_check_validator():
#     return validator("unit", allow_reuse=True)(dBc_unit_check)


# # ----------------------------------------------------------------------


# def dBm_unit_check(unit: str) -> None:
#     if unit != "dBm":
#         raise ValueError("unit: {unit}, must be dBm".format(unit=unit))


# def dBm_unit_check_validator():
#     return validator("unit", allow_reuse=True)(dBm_unit_check)


# # ----------------------------------------------------------------------


# def dBW_unit_check(unit: str) -> None:
#     if unit != "dBW":
#         raise ValueError("unit: {unit}, must be dBW".format(unit=unit))


# def dBW_unit_check_validator():
#     return validator("unit", allow_reuse=True)(dBW_unit_check)
