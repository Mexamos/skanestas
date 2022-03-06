from typing import List, Tuple

from clickhouse_driver import Client

from settings import CLICKHOUSE_URI, CLICKHOUSE_DB, CLICKHOUSE_TABLE, TRACK_NAMES

clickhouse_client = Client.from_url(CLICKHOUSE_URI)


def create_table() -> None:
    execute_str = f'''
        CREATE TABLE IF NOT EXISTS {CLICKHOUSE_DB}.{CLICKHOUSE_TABLE} (
            datetime DateTime DEFAULT now(), name String, price Int32
        ) ENGINE = MergeTree() ORDER BY datetime
    '''
    clickhouse_client.execute(execute_str)


def insert_prices(values) -> None:
    clickhouse_client.execute(
        f'INSERT INTO {CLICKHOUSE_DB}.{CLICKHOUSE_TABLE} (name, price) VALUES', values
    )


def insert_start_prices() -> None:
    row = clickhouse_client.execute(f'SELECT * FROM {CLICKHOUSE_DB}.{CLICKHOUSE_TABLE} LIMIT 1')
    if len(row) == 0:
        start_values = [{'name': name, 'price': 0} for name in TRACK_NAMES]
        insert_prices(start_values)


def init_db() -> None:
    create_table()
    insert_start_prices()


def get_latest_tracks_prices() -> List[Tuple[str, int]]:
    rows = clickhouse_client.execute(
        f'''
            SELECT t1.name, t1.price
            FROM {CLICKHOUSE_DB}.{CLICKHOUSE_TABLE} t1
            INNER JOIN (
                SELECT name, max(datetime) as latest_date
                FROM {CLICKHOUSE_DB}.{CLICKHOUSE_TABLE}
                GROUP BY name
            ) t2 ON t1.name = t2.name AND t1.datetime = t2.latest_date ORDER BY name
        '''
    )
    return rows
