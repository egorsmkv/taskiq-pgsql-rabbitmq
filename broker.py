from taskiq_aio_pika import AioPikaBroker
from taskiq_psqlpy import PSQLPyResultBackend

psqlpy_result_backend = PSQLPyResultBackend(
    dsn="postgres://my_user:password@localhost:5432/my_db",
)

broker = AioPikaBroker(
    url="amqp://guest:guest@localhost:5672",
    qos=1,
)
broker.with_result_backend(psqlpy_result_backend)
