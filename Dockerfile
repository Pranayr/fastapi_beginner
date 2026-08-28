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

# Copy dependency files first
# This allows Docker to cache the dependency installation layer
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy application code
COPY . .

# Make startup script executable
RUN chmod +x /app/boot/docker-run.sh

EXPOSE 8000

# Start application using startup script
CMD ["/app/boot/docker-run.sh"]