import os
import argparse
import pandas as pd
from collections import defaultdict
from utils.portfolio_optimizer import PortfolioOptimizer
from utils.llm import generate_insights
from utils.tickers import TickerData
from utils.utilities import save_fig
from utils.report import generate_report
from datetime import date
from dateutil.relativedelta import relativedelta

def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    os.makedirs("plots", exist_ok=True)
    
    datares = defaultdict(dict)
    parser = argparse.ArgumentParser(
        description="Portfolio Optimization and Management using PortfolioOptimizer Framework"
    )
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "--data",
        type=str,
        help="Path to CSV file containing asset returns (dates as index)"
    )
    group.add_argument(
        "--tickers",
        type=str,
        nargs="+",
        help="List of tickers to include in the analysis"
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
    parser.add_argument(
        "--start",
        type=str,
        help="Start date for data retrieval (required if --tickers is provided)"
    )
    parser.add_argument(
        "--end",
        type=str,
        help="End date for data retrieval (required if --tickers is provided)"
    )
    
    args = parser.parse_args()

    if args.data:
        try:
            data = pd.read_csv(args.data, index_col=0, parse_dates=True)
        except Exception as e:
            print(f"Error loading data: {e}")
            return
    elif args.tickers:
        if not args.start or not args.end:    
            args.end = date.today()
            args.start = (args.end - relativedelta(years=2))

            args.start = args.start.strftime('%Y-%m-%d')
            args.end = args.end.strftime('%Y-%m-%d')

        try:
            tick=TickerData(args.tickers, args.start, args.end)
            data = tick.ticker_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            return

    optimizer = PortfolioOptimizer(data, risk_free_rate=args.riskfree)

    # ---------------------------
    # Run Various Optimizations
    # ---------------------------
    '''Maximum Sharpe Ratio Optimization'''
    ms_weights, ms_ret, ms_vol = optimizer.maximize_sharpe_ratio()
    optimizer.add_weights('Maximum Sharpe Ratio')
    datares['Maximum Sharpe Ratio']['Weights'] = ms_weights
    datares['Maximum Sharpe Ratio']['Annualized Return'] = ms_ret
    datares['Maximum Sharpe Ratio']['Annualized Volatility'] = ms_vol

    '''Minimum Volatility Optimization'''
    mv_weights, mv_ret, mv_vol = optimizer.minimize_volatility()
    optimizer.add_weights('Minimum Volatility')
    datares['Minimum Volatility']['Weights'] = mv_weights
    datares['Minimum Volatility']['Annualized Return'] = mv_ret
    datares['Minimum Volatility']['Annualized Volatility'] = mv_vol

    '''Hierarchical Risk Parity (HRP) Optimization'''
    hrp_weights, hrp_ret, hrp_vol = optimizer.hierarchical_risk_parity()
    optimizer.add_weights('Hierarchical Risk Parity')
    datares['Hierarchical Risk Parity']['Weights'] = hrp_weights
    datares['Hierarchical Risk Parity']['Annualized Return'] = hrp_ret
    datares['Hierarchical Risk Parity']['Annualized Volatility'] = hrp_vol

    '''Equal Risk Contribution (ERC) Optimization'''
    erc_weights, erc_ret, erc_vol = optimizer.equal_risk_contribution()
    optimizer.add_weights('Equal Risk')
    datares['Equal Risk']['Weights'] = erc_weights
    datares['Equal Risk']['Annualized Return'] = erc_ret
    datares['Equal Risk']['Annualized Volatility'] = erc_vol

    '''Equal Weight Portfolio'''
    eq_weights, eq_ret, eq_vol = optimizer.equal_weight()
    optimizer.add_weights('Equal Weight')
    datares['Equal Weight']['Weights'] = eq_weights
    datares['Equal Weight']['Annualized Return'] = eq_ret
    datares['Equal Weight']['Annualized Volatility'] = eq_vol

    '''Maximum Diversification Optimization'''
    md_weights, md_ret, md_vol = optimizer.maximum_diversification()
    optimizer.add_weights('Maximum Diversification')
    datares['Maximum Diversification']['Weights'] = md_weights
    datares['Maximum Diversification']['Annualized Return'] = md_ret
    datares['Maximum Diversification']['Annualized Volatility'] = md_vol

    '''Minimum CVaR Optimization'''
    mcvar_weights, mcvar_ret, mcvar_vol = optimizer.minimize_cvar(alpha=0.05)
    optimizer.add_weights('Minimum CVaR')
    datares['Minimum CVaR']['Weights'] = mcvar_weights
    datares['Minimum CVaR']['Annualized Return'] = mcvar_ret
    datares['Minimum CVaR']['Annualized Volatility'] = mcvar_vol

    '''Backtesting'''
    if args.backtest:
        for i in ['max_sharpe', 'min_vol', 'HRP', 'ERC', 'Eq', 'max_div', 'min_cvar']:
            results = optimizer.backtest_portfolio(
                start_date=data.index[0],
                end_date=data.index[-1],
                train_window=252,
                rebalance_period=63,
                optimization_method=i,
                transaction_cost=0.001,)
            datares['backtesting'][i] = results[2]
            save_fig(results[3], f"plots/{i}_backtest.png")


    '''Visualization'''
    if args.plots:
        #ef=optimizer.plot_efficient_frontier()
        pa=optimizer.plot_portfolio_allocation()
        rc=optimizer.plot_risk_contributions()
        cr=optimizer.plot_cumulative_returns()
        cm=optimizer.plot_correlation_matrix()
        sdr=optimizer.simulate_random_portfolios()

        #save_fig(ef, "plots/efficient_frontier.png")

        for i in pa.keys():
            save_fig(pa[i], f"plots/{i}_portfolio_allocation.png")
        for i in rc.keys():
            save_fig(rc[i], f"plots/{i}_risk_contributions.png")
        for i in cr.keys():
            save_fig(cr[i], f"plots/{i}_cumulative_returns.png")
        save_fig(cm, f"plots/correl_mat.png")
        save_fig(sdr[0], "plots/simulate_random_portfolios.png")
        save_fig(sdr[1], "plots/distribution_sharpe_ratios.png")
        
    '''Sensitivity'''
    if args.sensitivity:
        for i in ['max_sharpe', 'min_vol', 'HRP', 'ERC', 'Eq', 'max_div', 'min_cvar']:
            sens = optimizer.sensitivity_analysis(
                train_windows=[252, 126],
                rebalance_periods=[63, 21],
                optimization_method=i
            )
            datares['Sensitivity Analysis'][i] = sens

    '''LLM Analysis using GPT O3 Mini'''
    if args.llm:
        insights = generate_insights(datares)
        '''include insights in final report'''
    else:
        '''create final report without llm'''
        generate_report(datares, args.tickers)


if __name__ == "__main__":
    main()
