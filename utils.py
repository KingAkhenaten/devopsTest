import yfinance as yf
from json import dumps


def get_finance_data(ticker: str):
    data = yf.Ticker(ticker)
    return dumps(data.info)