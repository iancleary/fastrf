from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app: FastAPI = FastAPI(
    on_startup=[lambda: print("Starting up!")],
    on_shutdown=[lambda: print("Shutting down!")],
)

# enable CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
