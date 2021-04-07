# isort:skip_file

from fastrf.app.application import app
from fastrf.app.routes.noise_figure import router as noise_figure_router
from fastrf.app.routes.gain_transfer import router as gain_transfer_router


ROUTERS = (noise_figure_router, gain_transfer_router)

for r in ROUTERS:
    app.include_router(r)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
