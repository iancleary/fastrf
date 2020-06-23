# testing

## App

We use `pytest`, [httpx](https://github.com/encode/httpx/), [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio), and [asgi-lifespan](https://github.com/florimondmanca/asgi-lifespan) to set up a test application.

Please walk through the [example from asgi-lifespan](https://github.com/florimondmanca/asgi-lifespan#sending-lifespan-events-for-testing), as it does a fantastic job setting up how a Starlette application is used!

> FastRF/FastAPI application directly inherit from Starlette!

### Client Setup

> Our goal is to have a pytest fixture that is a client that can send requests to our application.  This will also mimic the `main.py` application that comes with fastrf

The main differences from the [example from asgi-lifespan](https://github.com/florimondmanca/asgi-lifespan#sending-lifespan-events-for-testing) are highlighted below.

```Python hl_lines="4 5 15 16 17 18 28"
import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastrf.app.main import app
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
```

We now have an asynchronous HTTP client as a `pytest` fixture! 🎉 🙌
