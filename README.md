# Evidence Storage Service

A lightweight DevOps-oriented microservice for storing and retrieving evidences using a cloud-like architecture locally with Docker, Azurite, and optional Swarm orchestration.

---

## Overview

This project implements a simple Evidence Storage API that allows:

- Storing JSON payloads as evidences
- Retrieving stored evidences by ID
- Running locally with Docker
- Simulating Azure Blob Storage using Azurite
- Deploying with Docker Compose and Docker Swarm

---

## Architecture

The system is composed of the following components:

- **FastAPI Service** (Python)
- **Azure Blob Storage Emulator (Azurite)**
- **Docker Compose for local orchestration**
- **Docker Swarm for clustered deployment**

### Flow

Client → FastAPI → Storage Client → Azurite (Blob Storage)

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Azure Storage SDK
- Docker
- Docker Compose
- Docker Swarm (optional)
- Pytest

---

## Project Structure

```
app/
 ├── api/            # HTTP routes
 ├── clients/        # Storage abstraction layer
 ├── core/           # Configuration
 ├── services/       # Business logic
 └── main.py

docker/
 └── entrypoint.sh

tests/

docker-compose.yml
docker-stack.yml
Dockerfile
Makefile
pyproject.toml
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
AZURE_CONNECTION_STRING=DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=...;BlobEndpoint=http://azurite:10000/devstoreaccount1;
CONTAINER_NAME=evidences
```

---

## How to Run Locally

### 1. Install dependencies

```bash
make install
```

---

### 2. Run API locally

```bash
make run
```

API available at:
```
http://localhost:8000/docs
```

---

## Run Tests

```bash
make test
```

---

## Docker

### Build image

```bash
make build
```

### Run with Docker Compose

```bash
make up
```

This starts:

- FastAPI service (port 8000)
- Azurite (port 10000)

---

### Stop services

```bash
make down
```

---

## Docker Swarm (Optional)

### Initialize Swarm

```bash
docker swarm init
```

### Deploy stack

```bash
make swarm-deploy
```

### Remove stack

```bash
make swarm-down
```

---

## API Endpoints

### Create Evidence

```
POST /api/evidence
```

Request:
```json
{
  "message": "example evidence"
}
```

Response:
```json
{
  "id": "generated-id"
}
```

---

### Get Evidence

```
GET /api/evidence/{id}
```

Response:
```json
{
  "data": {
    "message": "example evidence"
  }
}
```

---

### Health Check

```
GET /health
```

---

## Services

| Service   | Description                  |
|----------|------------------------------|
| app      | FastAPI microservice         |
| azurite  | Azure Storage emulator       |

---

## Makefile Commands

```bash
make install        # install dependencies
make run            # run API locally
make test           # run tests
make build          # build docker image
make up             # docker compose up
make down           # docker compose down
make swarm-deploy   # deploy swarm stack
make swarm-down     # remove swarm stack
```

---

## Future Improvements

- Add authentication (JWT)
- Add OpenTelemetry tracing
- Add CI/CD pipeline (GitHub Actions)
- Deploy to real Azure Storage
