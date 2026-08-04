import os


WORKERS_NUM = 0
MAX_CHUNK_SIZE = 2**16
_request_timeout = os.getenv("AIS_BENCH_REQUEST_TIMEOUT")
REQUEST_TIME_OUT = float(_request_timeout) if _request_timeout else None

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = INFO # log level, choose from DEBUG, INFO, WARNING, ERROR, CRITICAL
