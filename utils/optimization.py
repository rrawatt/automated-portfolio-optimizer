# optimization.py
import numpy as np
import scipy.optimize as sco
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import squareform

class OptimizationMixin:
    def minimize_volatility(self):
        """Optimize portfolio to minimize volatility."""
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        init_guess = np.array([1.0 / self.num_assets] * self.num_assets)
        result = sco.minimize(lambda x: self.calculate_portfolio_performance(x)[1],
                              init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def maximize_sharpe_ratio(self):
        """Optimize portfolio to maximize Sharpe ratio."""
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        init_guess = np.array([1.0 / self.num_assets] * self.num_assets)
        result = sco.minimize(lambda x: -self.calculate_sharpe_ratio(x),
                              init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def hierarchical_risk_parity(self):
        """Optimize portfolio using Hierarchical Risk Parity (HRP)."""
        corr = self.returns.corr()
        dist = np.sqrt(0.5 * (1 - corr))
        dist_condensed = squareform(dist.values, checks=False)
        link = linkage(dist_condensed, method='single')
        order = list(leaves_list(link))
        weights = np.ones(self.num_assets)
        clusters = [order]
        while clusters:
            cluster = clusters.pop(0)
            if len(cluster) > 1:
                mid = len(cluster) // 2
                left = cluster[:mid]
                right = cluster[mid:]
                left_risk = self._calculate_cluster_risk(left)
                right_risk = self._calculate_cluster_risk(right)
                alloc_factor = 1.0 - left_risk / (left_risk + right_risk)
                for i in left:
                    weights[i] *= alloc_factor
                for i in right:
                    weights[i] *= (1 - alloc_factor)
                clusters.append(left)
                clusters.append(right)
        weights /= np.sum(weights)
        self.weights = weights
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def equal_risk_contribution(self):
        """Optimize portfolio using Equal Risk Contribution (ERC)."""
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        init_guess = np.array([1.0 / self.num_assets] * self.num_assets)
        result = sco.minimize(lambda x: self._erc_objective(x),
                              init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def minimize_cvar(self, alpha=0.05):
        """Optimize portfolio to minimize Conditional VaR."""
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        init_guess = np.array([1.0 / self.num_assets] * self.num_assets)
        result = sco.minimize(lambda w: self.calculate_cvar(w, alpha), 
                              init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def equal_weight(self):
        """Construct an equal weight portfolio."""
        weights = np.array([1.0 / self.num_assets] * self.num_assets)
        self.weights = weights
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def maximum_diversification(self):
        """Optimize portfolio by maximizing the diversification ratio."""
        sigma = self.returns.std() * np.sqrt(252)
        def objective(w):
            port_vol = np.sqrt(np.dot(w.T, np.dot(self.cov_matrix, w)))
            return - np.dot(w, sigma) / port_vol  # Negative for maximization
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        init_guess = np.array([1.0 / self.num_assets] * self.num_assets)
        result = sco.minimize(objective, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        return self.weights, *self.calculate_portfolio_performance(self.weights)

    def optimize_black_litterman(self, views=None, tau=0.025):
        """Stub for Black–Litterman optimization."""
        print("Black–Litterman optimization not fully implemented. Returning max_sharpe results.")
        return self.maximize_sharpe_ratio()

    # --- Helper Methods ---
    def _calculate_cluster_risk(self, indices):
        cov = self.returns.cov() * 252
        cluster_weights = np.ones(len(indices))
        cluster_weights /= np.sum(cluster_weights)
        cluster_cov = cov.iloc[indices, indices]
        risk = np.sqrt(np.dot(cluster_weights.T, np.dot(cluster_cov, cluster_weights)))
        return risk

    def _erc_objective(self, weights):
        risk_contrib = self._calculate_risk_contributions(weights)
        return np.sum((risk_contrib - np.mean(risk_contrib)) ** 2)

    def _calculate_risk_contributions(self, weights):
        cov_matrix = self.returns.cov() * 252
        port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        marginal = np.dot(cov_matrix, weights) / port_vol
        return weights * marginal
