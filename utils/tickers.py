"""
Module: tickers.py

Purpose:
    Handles the retrieval and validation of financial ticker data using the yfinance library.
    Downloads historical price data and converts it into returns while addressing outliers.

Classes:
    TickerData:
        Constructor:
            - __init__(tickers, start_date, end_date):
                  Initializes the instance with a list of ticker symbols and a date range.
        Methods:
            - check_ticker(ticker_symbol):
                  Checks if a given ticker symbol is valid by attempting to access its information.
            - check_tickers():
                  Iterates over all tickers and returns a list of invalid ones, if any.
            - ticker_data():
                  If all tickers are valid, downloads historical price data for the tickers,
                  computes daily returns from closing prices, identifies outliers using z-scores,
                  and replaces outliers with the column mean. Returns the processed returns DataFrame.
"""


import yfinance as yf
import pandas as pd
import numpy as np

class TickerData:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
    
    def check_ticker(self, ticker_symbol):
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
        if self.check_tickers():
            return f"Invalid tickers: {self.check_tickers()}"
        else:
            # Fix: Download price data
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
            
            # Fix: Calculate returns instead of using raw prices
            prices = data['Close']
            
            # Convert to returns
            returns = prices.pct_change().dropna()
            
            # Detect and handle outliers
            z_scores = np.abs((returns - returns.mean()) / returns.std())
            outliers = z_scores > 3
            
            # Replace outliers with column means
            for col in returns.columns:
                col_outliers = outliers[col]
                if col_outliers.any():
                    returns.loc[col_outliers, col] = returns[col].mean()
                    
            return returns