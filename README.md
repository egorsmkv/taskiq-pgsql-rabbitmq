# Taskiq: PgSQL + RabbitMQ

## Env

```
uv venv --python 3.12

source .venv/bin/activate

uv sync
```

## Run PostgreSQL & RabbitMQ

```
docker compose -f compose-dev.yml up
```

## Start workers

```
uv run taskiq worker broker:broker --fs-discover --workers 5
```

## Create tasks

```
python create_tasks.py
```

## Dev

```
uv pip install ruff

ruff check --select I --fix
ruff format
```

If you want to see the results:

```
docker exec -it pgsql_dev psql -U my_user -d my_db
```
