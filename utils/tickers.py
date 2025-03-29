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