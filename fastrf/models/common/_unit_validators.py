from pydantic import validator


def dB_unit_check(unit: str) -> None:
    if unit != "dB":
        raise ValueError("unit: {unit}, must be dB".format(unit=unit))


def dB_unit_check_validator():
    return validator("unit", allow_reuse=True)(dB_unit_check)


# ----------------------------------------------------------------------


def dBc_unit_check(unit: str) -> None:
    if unit != "dBc":
        raise ValueError("unit: {unit}, must be dBc".format(unit=unit))


def dBc_unit_check_validator():
    return validator("unit", allow_reuse=True)(dBc_unit_check)


# ----------------------------------------------------------------------


def dBm_unit_check(unit: str) -> None:
    if unit != "dBm":
        raise ValueError("unit: {unit}, must be dBm".format(unit=unit))


def dBm_unit_check_validator():
    return validator("unit", allow_reuse=True)(dBm_unit_check)


# ----------------------------------------------------------------------


def dBW_unit_check(unit: str) -> None:
    if unit != "dBW":
        raise ValueError("unit: {unit}, must be dBW".format(unit=unit))


def dBW_unit_check_validator():
    return validator("unit", allow_reuse=True)(dBW_unit_check)
