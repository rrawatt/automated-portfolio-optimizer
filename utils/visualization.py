# visualization.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class VisualizationMixin:
    def plot_efficient_frontier(self, num_portfolios=1000, save_path=None):
        """Plot the efficient frontier by simulating random portfolios."""
        results = np.zeros((3, num_portfolios))
        for i in range(num_portfolios):
            w = np.random.random(self.num_assets)
            w /= np.sum(w)
            ret, vol = self.calculate_portfolio_performance(w)
            results[0, i] = ret
            results[1, i] = vol
            results[2, i] = self.calculate_sharpe_ratio(w)
        plt.figure(figsize=(10, 6))
        plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap="viridis", marker="o")
        plt.xlabel("Annualized Volatility")
        plt.ylabel("Annualized Return")
        plt.title("Efficient Frontier")
        plt.colorbar(label="Sharpe Ratio")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

    def plot_portfolio_allocation(self, save_path=None):
        """Plot the current portfolio allocation as a bar chart."""
        if self.weights is None:
            print("Run an optimization method first to get weights.")
            return
        assets = self.returns.columns.tolist()
        plt.figure(figsize=(8, 5))
        plt.bar(assets, self.weights, color="skyblue", edgecolor="black")
        plt.xlabel("Assets")
        plt.ylabel("Weight")
        plt.title("Portfolio Allocation")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

    def plot_risk_contributions(self, weights=None, save_path=None):
        """Plot the risk contributions of each asset."""
        if weights is None:
            weights = self.weights
        if weights is None:
            print("Run an optimization method first.")
            return
        risk_contrib = self._calculate_risk_contributions(weights)
        assets = self.returns.columns.tolist()
        plt.figure(figsize=(8, 5))
        plt.bar(assets, risk_contrib, color="coral", edgecolor="black")
        plt.xlabel("Assets")
        plt.ylabel("Risk Contribution")
        plt.title("Risk Contributions")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

    def plot_cumulative_returns(self, weights=None, save_path=None):
        """Plot cumulative portfolio returns over time."""
        if weights is None:
            weights = self.weights
        if weights is None:
            print("Run an optimization method first.")
            return
        port_returns = self.returns @ weights
        cum_returns = np.cumprod(1 + port_returns) - 1
        plt.figure(figsize=(10, 6))
        plt.plot(cum_returns, color="green")
        plt.xlabel("Time")
        plt.ylabel("Cumulative Return")
        plt.title("Cumulative Portfolio Returns")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

    def plot_correlation_matrix(self, save_path=None):
        """Plot a heatmap of the asset return correlation matrix."""
        corr = self.returns.corr()
        plt.figure(figsize=(8, 6))
        plt.imshow(corr, cmap="coolwarm", interpolation="none")
        plt.colorbar()
        plt.xticks(range(len(corr)), corr.columns, rotation=90)
        plt.yticks(range(len(corr)), corr.columns)
        plt.title("Correlation Matrix")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

    def simulate_random_portfolios(self, num_portfolios=5000, save_path=None):
        """Simulate random portfolios and plot their risk-return distribution."""
        results = np.zeros((3, num_portfolios))
        weight_records = []
        for i in range(num_portfolios):
            w = np.random.random(self.num_assets)
            w /= np.sum(w)
            weight_records.append(w)
            ret, vol = self.calculate_portfolio_performance(w)
            results[0, i] = ret
            results[1, i] = vol
            results[2, i] = self.calculate_sharpe_ratio(w)
        plt.figure(figsize=(12, 8))
        plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap="viridis", marker="o")
        plt.xlabel("Annualized Volatility")
        plt.ylabel("Annualized Return")
        plt.title("Random Portfolios Simulation")
        plt.colorbar(label="Sharpe Ratio")
        plt.show()
        plt.figure(figsize=(10, 6))
        plt.hist(results[2, :], bins=50, color="skyblue", edgecolor="black")
        plt.xlabel("Sharpe Ratio")
        plt.ylabel("Frequency")
        plt.title("Distribution of Sharpe Ratios")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
        return results, weight_records

    def plot_allocation_over_time(self, save_path=None):
        """Plot the evolution of portfolio weights over time."""
        if not self.weight_history:
            print("No allocation history available. Run a backtest first.")
            return
        dates = list(self.weight_history.keys())
        allocations = np.array([self.weight_history[d] for d in dates])
        assets = self.returns.columns.tolist()
        plt.figure(figsize=(10, 6))
        for i in range(self.num_assets):
            plt.plot(dates, allocations[:, i], label=assets[i])
        plt.xlabel("Rebalance Date")
        plt.ylabel("Weight")
        plt.title("Portfolio Allocation Over Time")
        plt.legend()
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
