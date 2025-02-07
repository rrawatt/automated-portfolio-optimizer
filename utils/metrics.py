# metrics.py
import numpy as np
import pandas as pd

class MetricsMixin:
    def calculate_portfolio_performance(self, weights):
        """Calculate annualized return and volatility."""
        annual_return = np.sum(self.returns.mean() * weights) * 252
        annual_vol = np.sqrt(np.dot(weights.T, np.dot(self.returns.cov() * 252, weights)))
        return annual_return, annual_vol

    def calculate_sharpe_ratio(self, weights):
        """Calculate the Sharpe ratio."""
        ret, vol = self.calculate_portfolio_performance(weights)
        return (ret - self.risk_free_rate) / vol

    def calculate_sortino_ratio(self, weights, target_return=0.0):
        """Calculate the Sortino ratio."""
        ret, _ = self.calculate_portfolio_performance(weights)
        downside = np.minimum(self.returns @ weights - target_return, 0)
        downside_vol = np.sqrt(np.mean(downside ** 2)) * np.sqrt(252)
        return (ret - self.risk_free_rate) / downside_vol

    def calculate_max_drawdown(self, weights):
        """Calculate the maximum drawdown."""
        port_returns = self.returns @ weights
        cumulative = np.cumprod(1 + port_returns) - 1
        peak = np.maximum.accumulate(cumulative)
        drawdowns = (peak - cumulative) / peak
        return np.nanmax(drawdowns)

    def calculate_var(self, weights, alpha=0.05):
        """Calculate Value at Risk (VaR)."""
        port_returns = self.returns @ weights
        return np.percentile(port_returns, alpha * 100)

    def calculate_cvar(self, weights, alpha=0.05):
        """Calculate Conditional Value at Risk (CVaR)."""
        port_returns = self.returns @ weights
        var = self.calculate_var(weights, alpha)
        return port_returns[port_returns <= var].mean()
