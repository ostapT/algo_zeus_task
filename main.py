import os

import requests
from datetime import datetime

from binance.client import Client
import csv

from binance.exceptions import BinanceAPIException

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
client = Client(api_key, api_secret)
SYMBOLS = [
    "stellar",
    "vechain",
    "uniswap",
    "dogecoin",
    "litecoin",
    "eos",
    "dash",
    "tezos",
    "iota",
    "monero",
]


def collect_data(symbol, interval):
    interval_mapper = {
        "1d": Client.KLINE_INTERVAL_1DAY,
        "1h": Client.KLINE_INTERVAL_1HOUR,
        "4h": Client.KLINE_INTERVAL_4HOUR
    }

    if interval in interval_mapper:
        interval = interval_mapper[interval]

    try:
        candles = client.get_klines(symbol=symbol, interval=interval)
    except BinanceAPIException as e:
        return f"API Error: {e.message}"

    write_to_csv(candles, symbol, interval)


def write_to_csv(candles, symbol, interval):
    fields = ["Open Time", "Open", "High", "Low", "Close", "Volume"]

    with open(f"{symbol}_{interval}_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(fields)

        for candle in candles:
            timestamp = int(candle[0])
            open_time = datetime.fromtimestamp(timestamp / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            data = [
                open_time,
                candle[1],
                candle[2],
                candle[3],
                candle[4],
                candle[5],
            ]
            writer.writerow(data)


def get_market_caps():
    market_caps = {}
    for symbol in SYMBOLS:
        url = (
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency="
            f"usd&ids={symbol}"
        )
        response = requests.get(url)
        data = response.json()
        market_cap = data[0]["market_cap"]
        market_caps[symbol] = market_cap

    return market_caps
