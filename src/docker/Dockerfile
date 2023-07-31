FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8

ARG UID="1000"
ARG GID="1000"
ARG USER="user"

WORKDIR /project/

ADD pyproject.toml /project
ADD poetry.lock /project
ADD docker/prod.env /project/.env

RUN addgroup --gid $GID $USER && \
    adduser --uid $UID --gid $GID --disabled-password --gecos '' $USER && \
    usermod -aG sudo $USER && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    pip install --upgrade pip && \
    pip install poetry==1.5.1 certifi && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    mkdir /data


COPY app /project/app
COPY data/quotes.json.gz /data

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /project/app

ENTRYPOINT ["/entrypoint.sh"]
