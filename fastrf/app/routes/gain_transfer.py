import uuid
from typing import Dict, List, Union

from fastapi import APIRouter

from fastrf.models.gain_transfer import Gain

router = APIRouter()


class GainSpec(Gain):
    id: str


gain_SPECS = [
    GainSpec(id=uuid.uuid4().hex, value=60.5),
    GainSpec(id=uuid.uuid4().hex, value=61.8),
    GainSpec(id=uuid.uuid4().hex, value=62.2),
]


@router.get("/gain", tags=["Gain"], response_model=List[GainSpec])
def get_all_gain_specs() -> List[Dict[str, Union[str, object]]]:
    # print(gain_SPECS)
    return [spec.dict(exclude={"unit"}) for spec in gain_SPECS]


@router.post("/gain", tags=["Gain"])
async def create_gain_spec(request: Gain) -> None:
    new_spec = GainSpec(id=uuid.uuid4().hex, value=request.value)
    gain_SPECS.append(new_spec)
    return


def remove_gain_spec(gain_spec_id: str) -> bool:
    # print(gain_SPECS)
    for spec in gain_SPECS:
        if spec.id == gain_spec_id:
            gain_SPECS.remove(spec)
            return True
    return False


@router.put(
    "/gain/{gain_id}",
    tags=["Gain"],
)
def edit_single_gain_spec(gain: Gain, gain_id: str) -> None:
    # Delete old entry
    remove_gain_spec(gain_id)
    # Add updated entry
    gain_SPECS.append(GainSpec(id=gain_id, value=gain.value))
    return


@router.delete(
    "/gain/{gain_id}",
    tags=["Gain"],
)
def remove_single_gain_spec(gain_id: str) -> None:
    remove_gain_spec(gain_id)
    return None
