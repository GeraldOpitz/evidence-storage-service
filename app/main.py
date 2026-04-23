from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Evidence Storage Service",
    description="""
A lightweight microservice for storing and retrieving evidence payloads.

## Features
- Store JSON evidences
- Retrieve evidences by ID
- List stored evidence IDs
- Health check endpoint

## Storage
This service uses Azurite as a local Azure Blob Storage emulator.
""",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Gerald Opitz",
    },
)

app.include_router(router)


@app.get(
    "/health",
    tags=["Health"],
    summary="Health check",
    description="Returns the current service health status."
)
def health():
    return {"status": "ok"}
