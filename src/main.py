from fastapi import FastAPI
from src.api.events.routing import router as event_router

app = FastAPI()
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}


"""
# FastAPI = web framework
# Uvicorn = web server

                    WEB SERVER
                  ┌─────────────┐
Browser ────────► │   Uvicorn   │
                  └──────┬──────┘
                         │
                         │ ASGI
                         ▼
                  ┌─────────────┐
                  │   FastAPI   │
                  │     app     │
                  └──────┬──────┘
                         │
                         ▼
                  Your Python code

Yes , you can remove uvicorn but, you still need an ASGI server (or another compatible server).
Uvicorn is just one ASGI server.
For example, you could use:
Uvicorn — most common for FastAPI development
Hypercorn

To run fastapi application:::: poetry run uvicorn main:app --reload

To build a docker:: docker build -t my-python-app .
To run the docker:: docker run --rm -p 8000:8000 my-python-app
To validate: http://localhost:8000


Old Docker file:

FROM python:3.12.8-slim

# Prevent Python from creating .pyc files
# and make stdout/stderr appear immediately in Docker logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install Poetry
ENV POETRY_VERSION=2.4.1 \
    POETRY_HOME=/opt/poetry

RUN python -m pip install --no-cache-dir poetry==${POETRY_VERSION}

# Add Poetry to PATH
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# Application directory
WORKDIR /app

# Tell Poetry to create the virtual environment inside the project
RUN poetry config virtualenvs.in-project true

#  Copy dependency files first
# This allows Docker to cache the dependency installation layer
COPY pyproject.toml poetry.lock ./

# Install dependencies
# --no-root means don't install the application itself as a package
RUN poetry install --no-root

# Copy the application code
COPY . .

EXPOSE 8000
# Run main.py using the Poetry environment
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

Docker Compose is a tool that lets you define and run multiple Docker containers as one application.
Instead of giving Docker a bunch of commands manually, you describe your application in a YAML file

Filename = compose.yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"

To run using <compose.yaml>, docker compose up 
to stop: docker compose down

=========
To keep the endpoint valid, we use pydantic, so that data to the endpoint and from the responses is valid
and raises errors if any.
"""