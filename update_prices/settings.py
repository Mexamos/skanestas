import os

CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER', 'admin')
CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD', 'admin')
CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST', 'clickhouse')
CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT', '9000')
CLICKHOUSE_DB = os.getenv('CLICKHOUSE_DB', 'db_name')
CLICKHOUSE_URI = f'clickhouse://{CLICKHOUSE_USER}:{CLICKHOUSE_PASSWORD}@' \
                f'{CLICKHOUSE_HOST}:{CLICKHOUSE_PORT}/{CLICKHOUSE_DB}'
CLICKHOUSE_TABLE = 'tracks'

TRACK_NAMES = [f'track_{str(i).zfill(2)}' for i in range(0, 100)]
