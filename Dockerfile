FROM python:3.13-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

COPY src/ src/
COPY alembic.ini alembic.ini
