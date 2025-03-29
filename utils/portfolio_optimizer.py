"""
Module: portfolio_optimizer.py

Purpose:
    Integrates multiple mixin classes to create a comprehensive PortfolioOptimizer class.
    This class is responsible for managing asset returns, performing optimizations, backtesting, visualization,
    metrics calculations, and various utility functions.

Classes:
    PortfolioOptimizer (inherits from MetricsMixin, OptimizationMixin, VisualizationMixin, BacktestingMixin, UtilityMixin):
        Constructor:
            - __init__(returns, risk_free_rate, cov_estimator):
                  Initializes the optimizer with asset return data, sets the risk-free rate, and computes the covariance matrix.
                  Ensures that the returns have a DateTime index and are sorted chronologically.
        Methods:
            - add_weights(opt):
                  Adds the computed weights from a given optimization method to an internal dictionary (weight_list) for further use.
"""


import pandas as pd
from .metrics import MetricsMixin
from .optimization import OptimizationMixin
from .visualization import VisualizationMixin
from .backtesting import BacktestingMixin
from .utilities import UtilityMixin

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
        '''self.weights_sr = None
        self.weights_vo = None
        self.weights_hrp = None
        self.weights_erc = None
        self.weights_eq = None
        self.weights_mdo = None
        self.weights_cvar = None'''
        self.weight_history = {}
        self.weight_list={}
        if cov_estimator is None:
            self.cov_matrix = self.returns.cov() * 252
        else:
            self.cov_matrix = cov_estimator(self.returns)

    def add_weights(self, opt):
        self.weight_list[opt]=self.weights