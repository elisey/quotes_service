# Service for serving ithappens.me quotes

## How to run in docker

```shell
cp docker/prod.env.example docker/prod.env
vim docker/prod.env
docker compose up --build -d
```

## Run tests and linters

```shell
task all
```