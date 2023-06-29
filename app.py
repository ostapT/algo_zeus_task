from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dotenv import load_dotenv
from main import collect_data, get_market_caps

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        interval = request.form["interval"]
        symbol = request.form["symbol"]
        if not symbol:
            symbol = "BTCUSDT"

        collect_data(symbol, interval)

        filename = f"{symbol}_{interval}_data.csv"
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError:
            error_message = (f"File '{filename}' not found. "
                             f"Please enter a valid symbol.")
            return render_template("index.html", error_message=error_message)

        candlestick_df = go.Figure(
            data=[
                go.Candlestick(
                    x=df["Open Time"],
                    open=df["Open"],
                    high=df["High"],
                    low=df["Low"],
                    close=df["Close"],
                )
            ],
            layout={
                "title": f"Candlestick Chart for {symbol} ({interval})",
                "xaxis": {"title": "Time"},
                "yaxis": {"title": "Price"},
            }
        )
        candlestick_json = candlestick_df.to_json()

        return render_template(
            "index.html",
            candlestick_data=candlestick_json,
            symbol=symbol,
            interval=interval
        )

    return render_template("index.html")


@app.route("/piechart", methods=["GET", "POST"])
def piechart():
    market_caps = get_market_caps()
    df_market_caps = pd.DataFrame(
        list(market_caps.items()),
        columns=["Symbol", "Market Cap"]
    )
    piechart_data = px.pie(
        df_market_caps,
        values="Market Cap",
        names="Symbol",
        title="Market Caps"
    )
    piechart_json = piechart_data.to_json()

    return render_template(
        "piechart.html",
        piechart_data=piechart_json
    )


if __name__ == "__main__":
    app.run()
