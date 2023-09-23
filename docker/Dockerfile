FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8

ARG UID="1000"
ARG GID="1000"
ARG USER="user"

WORKDIR /project/

COPY data/quotes.json.gz /data/quotes.json.gz
COPY pyproject.toml poetry.lock /project/
COPY docker/prod.env /project/.env

RUN addgroup --gid $GID $USER && \
    adduser --uid $UID --gid $GID --disabled-password --gecos '' $USER && \
    usermod -aG sudo $USER && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    pip install --upgrade pip && \
    pip install poetry==1.6.1 certifi && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    rm -rf /root/.cache && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY app /project/app


WORKDIR /project

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
