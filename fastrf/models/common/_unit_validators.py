from pydantic import validator


def dB_unit_check(unit: str) -> None:
    if unit != "dB":
        raise ValueError("unit: {unit}, must be dB".format(unit=unit))


def dB_unit_check_validator():  # type: ignore
    return validator("unit", allow_reuse=True)(dB_unit_check)


def power_unit_check(unit: str) -> None:
    allowed_power_units = {"W", "dBm", "dBW"}
    if unit not in allowed_power_units:
        raise ValueError(
            "unit: {unit}, must be in {allowed_power_units}".format(
                unit=unit, allowed_power_units=allowed_power_units
            )
        )


def power_unit_validator():  # type: ignore
    return validator("unit", allow_reuse=True)(power_unit_check)


def frequency_unit_check(unit: str) -> None:
    allowed_frequency_units = {"mHz", "Hz", "Khz", "MHz", "GHz", "THz"}
    if unit not in allowed_frequency_units:
        raise ValueError(
            "unit: {unit}, must be in {allowed_frequency_units}".format(
                unit=unit, allowed_frequency_units=allowed_frequency_units
            )
        )


def frequency_unit_validator():  # type: ignore
    return validator("unit", allow_reuse=True)(frequency_unit_check)


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
