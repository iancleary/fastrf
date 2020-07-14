import httpx
import pytest
from asgi_lifespan import LifespanManager

from fastrf.app.application import app
from fastrf.app.routes.noise_figure import router as noise_figure_router


@pytest.fixture
async def test_app():
    async def startup():
        print("Starting up")

    async def shutdown():
        print("Shutting down")

    ROUTERS = (noise_figure_router,)

    for r in ROUTERS:
        app.include_router(r)

    async with LifespanManager(app):
        print("We're in!")
        yield app


@pytest.fixture
async def client(test_app):
    async with httpx.AsyncClient(
        app=test_app, base_url="http://localhost:8888"
    ) as client:
        print("Client is ready")
        yield client


@pytest.mark.asyncio
async def test_docs(client):
    print("Testing")
    response = await client.get("/docs")
    assert response.status_code == 200
    print("OK")
