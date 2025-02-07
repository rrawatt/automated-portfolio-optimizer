# portfolio_optimizer.py
import pandas as pd
from metrics import MetricsMixin
from optimization import OptimizationMixin
from visualization import VisualizationMixin
from backtesting import BacktestingMixin
from utilities import UtilityMixin

class PortfolioOptimizer(MetricsMixin, 
                         OptimizationMixin, 
                         VisualizationMixin, 
                         BacktestingMixin, 
                         UtilityMixin):
    def __init__(self, returns, risk_free_rate=0.0, cov_estimator=None):
        """
        Initialize the PortfolioOptimizer with asset returns and settings.
        """
        self.returns = returns.copy()
        if not isinstance(self.returns.index, pd.DatetimeIndex):
            self.returns.index = pd.to_datetime(self.returns.index)
        self.returns.sort_index(inplace=True)
        self.risk_free_rate = risk_free_rate
        self.num_assets = self.returns.shape[1]
        self.weights = None
        self.weight_history = {}
        if cov_estimator is None:
            self.cov_matrix = self.returns.cov() * 252
        else:
            self.cov_matrix = cov_estimator(self.returns)
