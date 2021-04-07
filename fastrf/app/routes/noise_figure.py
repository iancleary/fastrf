import uuid
from typing import Dict, List, Union

from fastapi import APIRouter

from fastrf.models.noise_figure import NoiseFigure

router = APIRouter()


class NoiseFigureSpec(NoiseFigure):
    id: str


NOISE_FIGURE_SPECS = [
    NoiseFigureSpec(id=uuid.uuid4().hex, value=1.5),
    NoiseFigureSpec(id=uuid.uuid4().hex, value=1.8),
    NoiseFigureSpec(id=uuid.uuid4().hex, value=2.2),
]


@router.get(
    "/noise_figure", tags=["Noise Figure"], response_model=List[NoiseFigureSpec]
)
def get_all_noise_figure_specs() -> List[Dict[str, Union[str, object]]]:
    # print(NOISE_FIGURE_SPECS)
    return [spec.dict(exclude={"unit"}) for spec in NOISE_FIGURE_SPECS]


@router.post("/noise_figure", tags=["Noise Figure"])
async def create_noise_figure_spec(request: NoiseFigure) -> None:
    new_spec = NoiseFigureSpec(id=uuid.uuid4().hex, value=request.value)
    NOISE_FIGURE_SPECS.append(new_spec)
    return


def remove_noise_figure_spec(noise_figure_spec_id: str) -> bool:
    # print(NOISE_FIGURE_SPECS)
    for spec in NOISE_FIGURE_SPECS:
        if spec.id == noise_figure_spec_id:
            NOISE_FIGURE_SPECS.remove(spec)
            return True
    return False


@router.put(
    "/noise_figure/{noise_figure_id}",
    tags=["Noise Figure"],
)
def edit_single_noise_figure_spec(
    noise_figure: NoiseFigure, noise_figure_id: str
) -> None:
    # Delete old entry
    remove_noise_figure_spec(noise_figure_id)
    # Add updated entry
    NOISE_FIGURE_SPECS.append(
        NoiseFigureSpec(id=noise_figure_id, value=noise_figure.value)
    )
    return


@router.delete(
    "/noise_figure/{noise_figure_id}",
    tags=["Noise Figure"],
)
def remove_single_noise_figure_spec(noise_figure_id: str) -> None:
    remove_noise_figure_spec(noise_figure_id)
    return None
