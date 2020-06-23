# isort:skip_file

from .application import app
from .routes.noise_figure import router as noise_figure_router


ROUTERS = (noise_figure_router,)

for r in ROUTERS:
    app.include_router(r)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
