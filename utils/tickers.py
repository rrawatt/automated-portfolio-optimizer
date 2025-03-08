import yfinance as yf
import pandas as pd

class TickerData:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
    
    def check_ticker(self,ticker_symbol):
        try:
            stock = yf.Ticker(ticker_symbol)
            stock.info  
            return True 
        except Exception:
            return False

    def check_tickers(self):
        invalid_tickers = []
        for ticker in self.tickers:
            if not self.check_ticker(ticker):
                invalid_tickers.append(ticker)
        return invalid_tickers

    def ticker_data(self):
        if self.check_tickers() != [] :
            return f"Invalid tickers: {self.check_tickers()}"
        else:
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
            return data
    