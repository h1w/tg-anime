FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

ADD pyproject.toml /app
ADD alembic.ini /app

RUN pip install --upgrade pip
RUN pip install uv

RUN uv pip install . --system

COPY /app/* /app/app/
