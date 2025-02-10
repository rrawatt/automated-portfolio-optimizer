#!/usr/bin/env python
import argparse
import pandas as pd
from collections import defaultdict
from utils.portfolio_optimizer import PortfolioOptimizer
from utils.llm import generate_insights

def main():
    # Define command-line arguments.
    datares = defaultdict(dict)
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
    parser.add_argument(
        "--llm",
        action="store_true",
        help="Generate LLM analysis of the output using GPT O3 Mini"
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
    '''Maximum Sharpe Ratio Optimization'''
    ms_weights, ms_ret, ms_vol = optimizer.maximize_sharpe_ratio()
    datares['Maximum Sharpe Ratio Optimization']['Weights'] = ms_weights
    datares['Maximum Sharpe Ratio Optimization']['Annualized Return'] = ms_ret
    datares['Maximum Sharpe Ratio Optimization']['Annualized Volatility'] = ms_vol

    '''Minimum Volatility Optimization'''
    mv_weights, mv_ret, mv_vol = optimizer.minimize_volatility()
    datares['Minimum Volatility Optimization']['Weights'] = mv_weights
    datares['Minimum Volatility Optimization']['Annualized Return'] = mv_ret
    datares['Minimum Volatility Optimization']['Annualized Volatility'] = mv_vol

    '''Hierarchical Risk Parity (HRP) Optimization'''
    hrp_weights, hrp_ret, hrp_vol = optimizer.hierarchical_risk_parity()
    datares['Hierarchical Risk Parity Optimization']['Weights'] = hrp_weights
    datares['Hierarchical Risk Parity Optimization']['Annualized Return'] = hrp_ret
    datares['Hierarchical Risk Parity Optimization']['Annualized Volatility'] = hrp_vol

    '''Equal Risk Contribution (ERC) Optimization'''
    erc_weights, erc_ret, erc_vol = optimizer.equal_risk_contribution()
    datares['Equal Risk Contribution Optimization']['Weights'] = erc_weights
    datares['Equal Risk Contribution Optimization']['Annualized Return'] = erc_ret
    datares['Equal Risk Contribution Optimization']['Annualized Volatility'] = erc_vol

    '''Equal Weight Portfolio'''
    eq_weights, eq_ret, eq_vol = optimizer.equal_weight()
    datares['Equal Weight Portfolio']['Weights'] = eq_weights
    datares['Equal Weight Portfolio']['Annualized Return'] = eq_ret
    datares['Equal Weight Portfolio']['Annualized Volatility'] = eq_vol

    '''Maximum Diversification Optimization'''
    md_weights, md_ret, md_vol = optimizer.maximum_diversification()
    datares['Maximum Diversification Optimization']['Weights'] = md_weights
    datares['Maximum Diversification Optimization']['Annualized Return'] = md_ret
    datares['Maximum Diversification Optimization']['Annualized Volatility'] = md_vol

    '''Minimum CVaR Optimization'''
    mcvar_weights, mcvar_ret, mcvar_vol = optimizer.minimize_cvar(alpha=0.05)
    datares['Minimum CVaR Optimization']['Weights'] = mcvar_weights
    datares['Minimum CVaR Optimization']['Annualized Return'] = mcvar_ret
    datares['Minimum CVaR Optimization']['Annualized Volatility'] = mcvar_vol

    '''Backtesting'''
    if args.backtest:
        for i in ['max_sharpe', 'min_vol', 'HRP', 'ERC']:
            results = optimizer.backtest_portfolio(
                start_date=data.index[0],
                end_date=data.index[-1],
                train_window=252,
                rebalance_period=63,
                optimization_method=i,
                transaction_cost=0.001
            )
            datares['backtesting'][i] = results[2]

    '''Visualization'''
    if args.plots:
        optimizer.plot_efficient_frontier()
        optimizer.plot_portfolio_allocation()
        optimizer.plot_risk_contributions()
        optimizer.plot_cumulative_returns()
        optimizer.plot_correlation_matrix()
        optimizer.simulate_random_portfolios()

    '''Sensitivity'''
    if args.sensitivity:
        sens = optimizer.sensitivity_analysis(
            train_windows=[252, 126],
            rebalance_periods=[63, 21],
            optimization_method="max_sharpe"
        )
        datares['Sensitivity Analsysis'] = sens

    '''LLM Analysis using GPT O3 Mini'''
    if args.llm:
        insights = generate_insights(datares)
        '''include insights in final report'''
    else:
        '''create final report without llm'''
        pass

if __name__ == "__main__":
    main()
