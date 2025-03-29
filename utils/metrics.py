"""
Module: metrics.py

Purpose:
    Provides functions to calculate key performance metrics for a portfolio, including annualized return,
    volatility, Sharpe ratio, Sortino ratio, maximum drawdown, Value at Risk (VaR), and Conditional VaR (CVaR).

Classes:
    MetricsMixin:
        Methods:
            - _portfolio_performance(weights):
                  Computes unrounded annualized return and volatility based on the portfolio's returns.
            - calculate_portfolio_performance(weights):
                  Returns the rounded annualized return and volatility for reporting purposes.
            - _sharpe_ratio(weights):
                  Computes the unrounded Sharpe ratio using the portfolio’s performance and risk-free rate.
            - calculate_sharpe_ratio(weights):
                  Returns the rounded Sharpe ratio.
            - _sortino_ratio(weights, target_return):
                  Computes the unrounded Sortino ratio based on the portfolio’s returns.
            - calculate_sortino_ratio(weights, target_return):
                  Returns the rounded Sortino ratio.
            - calculate_max_drawdown(weights):
                  Calculates the maximum drawdown of the portfolio based on its cumulative returns.
            - calculate_var(weights, alpha):
                  Computes the Value at Risk (VaR) for the portfolio.
            - calculate_cvar(weights, alpha):
                  Computes the Conditional Value at Risk (CVaR) using the portfolio returns.
"""

import numpy as np

def _to_float(x):
    return float(round(x, 2))

class MetricsMixin:
    def _portfolio_performance(self, weights):
        """Calculate unrounded annualized return and volatility."""
        annual_return = np.sum(self.returns.mean() * weights) * 252
        cov_matrix = self.returns.cov() * 252
        annual_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return annual_return, annual_vol

    def calculate_portfolio_performance(self, weights):
        """Calculate rounded annualized return and volatility for reporting."""
        annual_return, annual_vol = self._portfolio_performance(weights)
        return _to_float(annual_return), _to_float(annual_vol)

    def _sharpe_ratio(self, weights):
        """Calculate unrounded Sharpe ratio using unrounded performance metrics."""
        ret, vol = self._portfolio_performance(weights)
        if vol == 0:
            return 0.001
        return (ret - self.risk_free_rate) / vol

    def calculate_sharpe_ratio(self, weights):
        return _to_float(self._sharpe_ratio(weights))

    def _sortino_ratio(self, weights, target_return=0.0):
        """Calculate unrounded Sortino ratio using unrounded performance metrics."""
        ret, _ = self._portfolio_performance(weights)
        port_returns = self.returns @ weights
        downside = np.minimum(port_returns - target_return, 0)
        downside_vol = np.sqrt(np.mean(downside ** 2)) * np.sqrt(252)
        if downside_vol == 0:
            return 0.001
        return (ret - target_return) / downside_vol

    def calculate_sortino_ratio(self, weights, target_return=0.0):
        return _to_float(self._sortino_ratio(weights, target_return))

    def calculate_max_drawdown(self, weights):
        port_returns = self.returns @ weights
        cumulative = np.cumprod(1 + port_returns) - 1
        peak = np.maximum.accumulate(cumulative)
        drawdowns = np.where(peak == 0, 0, (peak - cumulative) / peak)
        return _to_float(np.nanmax(drawdowns))

    def calculate_var(self, weights, alpha=0.05):
        port_returns = self.returns @ weights
        return _to_float(np.percentile(port_returns, alpha * 100))

    def calculate_cvar(self, weights, alpha=0.05):
        port_returns = self.returns @ weights
        var = self.calculate_var(weights, alpha)
        cvar_values = port_returns[port_returns <= var]
        if len(cvar_values) == 0:
            return 0.001
        return _to_float(np.mean(cvar_values))