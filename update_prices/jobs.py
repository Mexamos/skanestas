from random import random

from clickhouse import get_latest_tracks_prices, insert_prices


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement


def update_prices():
    tracks_prices = get_latest_tracks_prices()
    updated_prices = [{'name': item[0], 'price': item[1] + generate_movement()} for item in tracks_prices]
    insert_prices(updated_prices)
