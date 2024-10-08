# Taskiq: PgSQL + RabbitMQ

## Env

```
uv venv --python 3.12

source .venv/bin/activate

uv sync
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

ruff check
ruff format
```

Look into the tables:

```
docker exec -it pgsql_dev psql -U my_user -d my_db
```
