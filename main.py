import requests
from datetime import datetime

from binance.client import Client
import csv


def collect_data(apikey, secret, symbol="BTCUSDT", interval="1h"):
    client = Client(apikey, secret)
    if interval == "1d":
        interval = Client.KLINE_INTERVAL_1DAY
    elif interval == "1h":
        interval = Client.KLINE_INTERVAL_1HOUR
    elif interval == "4h":
        interval = Client.KLINE_INTERVAL_4HOUR

    candles = client.get_klines(symbol=symbol, interval=interval)
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
    symbols = [
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

    market_caps = {}
    for symbol in symbols:
        url = (
            f"https://api.coingecko.com/api/v3/coins/markets?vs_currency="
            f"usd&ids={symbol}"
        )
        response = requests.get(url)
        data = response.json()
        market_cap = data[0]["market_cap"]
        market_caps[symbol] = market_cap

    return market_caps
