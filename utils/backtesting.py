# backtesting.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class BacktestingMixin:
    def backtest_portfolio(self, start_date, end_date, train_window=252, rebalance_period=63,
                           optimization_method="max_sharpe", transaction_cost=0.0, benchmark=None):
        """Backtest the portfolio using a rolling window approach."""
        bt_data = self.returns.loc[start_date:end_date]
        n = bt_data.shape[0]
        portfolio_returns_list = []
        self.weight_history = {}
        prev_weights = None

        i = 0
        while i + train_window < n:
            train_data = bt_data.iloc[i : i + train_window]
            optimizer_train = self.__class__(train_data, risk_free_rate=self.risk_free_rate)
            optimizer_train.cov_matrix = self.cov_matrix.loc[train_data.columns, train_data.columns]
            if optimization_method == "max_sharpe":
                weights, _, _ = optimizer_train.maximize_sharpe_ratio()
            elif optimization_method == "min_vol":
                weights, _, _ = optimizer_train.minimize_volatility()
            elif optimization_method == "HRP":
                weights, _, _ = optimizer_train.hierarchical_risk_parity()
            elif optimization_method == "ERC":
                weights, _, _ = optimizer_train.equal_risk_contribution()
            else:
                raise ValueError("Unsupported optimization method.")

            if prev_weights is not None:
                turnover = self.calculate_turnover(prev_weights, weights)
                cost_adjustment = 1 - (turnover * transaction_cost)
            else:
                cost_adjustment = 1.0

            rebal_date = bt_data.index[i + train_window - 1]
            self.weight_history[rebal_date] = weights

            test_start = i + train_window
            test_end = min(i + train_window + rebalance_period, n)
            test_data = bt_data.iloc[test_start:test_end]
            p_returns = test_data.dot(weights) * cost_adjustment
            portfolio_returns_list.append(p_returns)
            prev_weights = weights
            i = test_end

        portfolio_returns = pd.concat(portfolio_returns_list).sort_index()
        cumulative_returns = (1 + portfolio_returns).cumprod() - 1

        ann_vol = portfolio_returns.std() * np.sqrt(252)
        ann_return = portfolio_returns.mean() * 252
        sharpe = (ann_return - self.risk_free_rate) / ann_vol

        cum_val = (1 + portfolio_returns).cumprod()
        roll_max = cum_val.cummax()
        drawdown = (cum_val - roll_max) / roll_max
        max_drawdown = drawdown.min()

        plt.figure(figsize=(10, 6))
        plt.plot(cum_val.index, cum_val, label="Portfolio Cumulative Return")
        if benchmark is not None:
            benchmark = benchmark.loc[cum_val.index]
            bench_cum = (1 + benchmark).cumprod()
            plt.plot(bench_cum.index, bench_cum, label="Benchmark", linestyle="--")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value")
        plt.title("Backtest: Cumulative Returns")
        plt.legend()
        plt.show()

        print(f"Total Return: {cumulative_returns.iloc[-1]:.2%}")
        print(f"Annualized Return: {ann_return:.2%}")
        print(f"Annualized Volatility: {ann_vol:.2%}")
        print(f"Sharpe Ratio: {sharpe:.2f}")
        print(f"Maximum Drawdown: {max_drawdown:.2%}")

        return portfolio_returns, cumulative_returns

    def sensitivity_analysis(self, train_windows=[252, 126], rebalance_periods=[63, 21],
                             optimization_method="max_sharpe"):
        """Run backtests over a range of parameters and print performance metrics."""
        results = []
        for tw in train_windows:
            for rp in rebalance_periods:
                print(f"\nBacktest with train_window = {tw} days, rebalance_period = {rp} days:")
                pr, cr = self.backtest_portfolio(start_date=self.returns.index[0],
                                                 end_date=self.returns.index[-1],
                                                 train_window=tw,
                                                 rebalance_period=rp,
                                                 optimization_method=optimization_method)
                ann_return = pr.mean() * 252
                ann_vol = pr.std() * np.sqrt(252)
                sharpe = (ann_return - self.risk_free_rate) / ann_vol
                cum_val = (1 + pr).cumprod()
                roll_max = cum_val.cummax()
                drawdown = (cum_val - roll_max) / roll_max
                max_dd = drawdown.min()
                results.append({
                    "Train Window": tw,
                    "Rebalance Period": rp,
                    "Annualized Return": ann_return,
                    "Annualized Volatility": ann_vol,
                    "Sharpe Ratio": sharpe,
                    "Max Drawdown": max_dd
                })
        results_df = pd.DataFrame(results)
        print("\nSensitivity Analysis Results:")
        print(results_df)
        return results_df
