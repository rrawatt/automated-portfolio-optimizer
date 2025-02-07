#!/usr/bin/env python
import argparse
import pandas as pd
from utils.portfolio_optimizer import PortfolioOptimizer

def main():
    # Define command-line arguments.
    parser = argparse.ArgumentParser(
        description="Portfolio Optimization and Management using PortfolioOptimizer Framework"
    )
    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to CSV file containing asset returns (dates as index)"
    )
    parser.add_argument(
        "--riskfree",
        type=float,
        default=0.01,
        help="Risk-free rate (default: 0.01)"
    )
    parser.add_argument(
        "--backtest",
        action="store_true",
        help="Run backtest using a rolling window approach"
    )
    parser.add_argument(
        "--plots",
        action="store_true",
        help="Display various portfolio visualizations"
    )
    parser.add_argument(
        "--sensitivity",
        action="store_true",
        help="Run sensitivity analysis on training and rebalance window parameters"
    )
    args = parser.parse_args()

    # Load asset returns data.
    try:
        data = pd.read_csv(args.data, index_col=0, parse_dates=True)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Initialize the PortfolioOptimizer with the provided data and risk-free rate.
    optimizer = PortfolioOptimizer(data, risk_free_rate=args.riskfree)

    # ---------------------------
    # Run Various Optimizations
    # ---------------------------
    print("=== Maximum Sharpe Ratio Optimization ===")
    ms_weights, ms_ret, ms_vol = optimizer.maximize_sharpe_ratio()
    print("Weights:", ms_weights)
    print(f"Annualized Return: {ms_ret:.2%}, Annualized Volatility: {ms_vol:.2%}\n")

    print("=== Minimum Volatility Optimization ===")
    mv_weights, mv_ret, mv_vol = optimizer.minimize_volatility()
    print("Weights:", mv_weights)
    print(f"Annualized Return: {mv_ret:.2%}, Annualized Volatility: {mv_vol:.2%}\n")

    print("=== Hierarchical Risk Parity (HRP) Optimization ===")
    hrp_weights, hrp_ret, hrp_vol = optimizer.hierarchical_risk_parity()
    print("Weights:", hrp_weights)
    print(f"Annualized Return: {hrp_ret:.2%}, Annualized Volatility: {hrp_vol:.2%}\n")

    print("=== Equal Risk Contribution (ERC) Optimization ===")
    erc_weights, erc_ret, erc_vol = optimizer.equal_risk_contribution()
    print("Weights:", erc_weights)
    print(f"Annualized Return: {erc_ret:.2%}, Annualized Volatility: {erc_vol:.2%}\n")

    print("=== Equal Weight Portfolio ===")
    eq_weights, eq_ret, eq_vol = optimizer.equal_weight()
    print("Weights:", eq_weights)
    print(f"Annualized Return: {eq_ret:.2%}, Annualized Volatility: {eq_vol:.2%}\n")

    print("=== Maximum Diversification Optimization ===")
    md_weights, md_ret, md_vol = optimizer.maximum_diversification()
    print("Weights:", md_weights)
    print(f"Annualized Return: {md_ret:.2%}, Annualized Volatility: {md_vol:.2%}\n")

    print("=== Minimum CVaR Optimization ===")
    mcvar_weights, mcvar_ret, mcvar_vol = optimizer.minimize_cvar(alpha=0.05)
    print("Weights:", mcvar_weights)
    print(f"Annualized Return: {mcvar_ret:.2%}, Annualized Volatility: {mcvar_vol:.2%}\n")

    # ---------------------------
    # Optional: Backtesting
    # ---------------------------
    if args.backtest:
        print("=== Running Backtest (Max Sharpe) ===")
        bt_returns, bt_cum = optimizer.backtest_portfolio(
            start_date=data.index[0],
            end_date=data.index[-1],
            train_window=252,
            rebalance_period=63,
            optimization_method="max_sharpe",
            transaction_cost=0.001
        )

    # ---------------------------
    # Optional: Visualizations
    # ---------------------------
    if args.plots:
        print("=== Generating Visualizations ===")
        optimizer.plot_efficient_frontier()
        optimizer.plot_portfolio_allocation()
        optimizer.plot_risk_contributions()
        optimizer.plot_cumulative_returns()
        optimizer.plot_correlation_matrix()
        optimizer.simulate_random_portfolios()

    # ---------------------------
    # Optional: Sensitivity Analysis
    # ---------------------------
    if args.sensitivity:
        print("=== Running Sensitivity Analysis ===")
        optimizer.sensitivity_analysis(
            train_windows=[252, 126],
            rebalance_periods=[63, 21],
            optimization_method="max_sharpe"
        )

if __name__ == "__main__":
    main()
