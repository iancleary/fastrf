import uuid

from fastapi import APIRouter
from fastrf.models.noise_figure import NoiseFigureBase, NoiseFigureCreateIn


router = APIRouter()

class NoiseFigureSpec(NoiseFigureBase):
    id: str = None


NOISE_FIGURE_SPECS = [
    {
        "id": uuid.uuid4().hex,
        "unit": "dB",
        "value": 1.5,
    },
    {
        "id": uuid.uuid4().hex,
        "unit": "dB",
        "value": 1.8,
    },
    {
        "id": uuid.uuid4().hex,
        "unit": "dB",
        "value": 8.8,
    },
]


@router.get("/noise_figure", tags=["Noise Figure"])
def get_all_noise_figure_specs():
    response_object = {"status": "success"}
    response_object["noise_figure_specs"] = NOISE_FIGURE_SPECS
    return response_object

@router.post("/noise_figure", tags=["Noise Figure"])
async def create_noise_figure_spec(request: NoiseFigureCreateIn):
    response_object = {"status": "success"}
    print(request)
    new_spec = NoiseFigureSpec(
        id=uuid.uuid4().hex,
        value=request.value
    )
    NOISE_FIGURE_SPECS.append(new_spec.dict())
    response_object["message"] = "Noise Figure Spec added!"
    return response_object


def remove_noise_figure_spec(noise_figure_spec_id):
    print(NOISE_FIGURE_SPECS)
    for spec in NOISE_FIGURE_SPECS:
        if spec["id"] == noise_figure_spec_id:
            NOISE_FIGURE_SPECS.remove(spec)
            return True
    return False

@router.put("/noise_figure/{noise_figure_id}", tags=["Noise Figure"])
def single_noise_figure_spec(noise_figure:NoiseFigureCreateIn, noise_figure_id:str):
    response_object = {"status": "success"}
    remove_noise_figure_spec(noise_figure_id)
    NOISE_FIGURE_SPECS.append(NoiseFigureSpec(
        id=noise_figure_id,
        value=noise_figure.value
        )
    )
    response_object["message"] = "Noise Figure Spec updated!"
    return response_object

@router.delete("/noise_figure/{noise_figure_id}", tags=["Noise Figure"])
def single_noise_figure_spec(noise_figure_id:str):
    response_object = {"status": "success"}
    remove_noise_figure_spec(noise_figure_id)
    response_object["message"] = "Noise Figure Spec removed!"
    return response_object
