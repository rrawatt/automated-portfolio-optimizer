# app.py

from flask import Flask, render_template, request, url_for
import os
import uuid
from datetime import datetime
from utils.portfolio_optimizer import PortfolioOptimizer
from utils.tickers import TickerData
from utils.utilities import save_fig

app = Flask(__name__)
PLOT_DIR = os.path.join(app.static_folder, 'plots')
os.makedirs(PLOT_DIR, exist_ok=True)

# Minimum days for computations
MIN_BACKTEST_DAYS = 252 + 63
MIN_SENSITIVITY_DAYS = 126 + 21

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        run_id = uuid.uuid4().hex

        # — User inputs —
        tickers = request.form['tickers'].split()
        start, end = request.form['start'], request.form['end']
        riskfree = float(request.form['riskfree'])
        do_plots = 'plots' in request.form
        do_backtest = 'backtest' in request.form
        do_sensitivity = 'sensitivity' in request.form

        # — Load data and init optimizer —
        data = TickerData(tickers, start, end).ticker_data()
        days = len(data)
        optimizer = PortfolioOptimizer(data, risk_free_rate=riskfree)

        # — 1. Portfolio optimizations —
        strategies = [
            ('Maximum Sharpe Ratio', 'max_sharpe', optimizer.maximize_sharpe_ratio),
            ('Minimum Volatility',    'min_vol',    optimizer.minimize_volatility),
            ('Hierarchical Risk Parity','HRP',       optimizer.hierarchical_risk_parity),
            ('Equal Risk Contribution','ERC',        optimizer.equal_risk_contribution),
            ('Equal Weight',          'Eq',         optimizer.equal_weight),
            ('Maximum Diversification','max_div',    optimizer.maximum_diversification),
            ('Minimum CVaR',          'min_cvar',   lambda: optimizer.minimize_cvar(alpha=0.05)),
        ]
        opt = {}
        for name, key, func in strategies:
            weights, ret, vol = func()
            optimizer.add_weights(name)
            opt[name] = {
                'description': get_description(name),
                'return': round(ret, 2),
                'volatility': round(vol, 2),
                'weights': dict(zip(tickers, [round(w, 2) for w in weights]))
            }

        # — 2. Visualization —
        # Ensure viz.alg always exists to avoid Jinja undefined errors
        viz = {'alg': {}, 'correlation': None, 'random': {'scatter': None, 'histogram': None}}

        if do_plots:
            alloc = optimizer.plot_portfolio_allocation()
            rc    = optimizer.plot_risk_contributions()
            cr    = optimizer.plot_cumulative_returns()
            corr  = optimizer.plot_correlation_matrix()
            rand, hist = optimizer.simulate_random_portfolios()

            # per-method images
            for name in alloc.keys():
                alloc_file = f"{name}_alloc_{run_id}.png"
                risk_file  = f"{name}_risk_{run_id}.png"
                cum_file   = f"{name}_cum_{run_id}.png"
                save_fig(alloc[name], os.path.join(PLOT_DIR, alloc_file))
                save_fig(rc[name],    os.path.join(PLOT_DIR, risk_file))
                save_fig(cr[name],    os.path.join(PLOT_DIR, cum_file))
                viz['alg'][name] = {
                    'allocation': url_for('static', filename=f'plots/{alloc_file}'),
                    'risk':       url_for('static', filename=f'plots/{risk_file}'),
                    'cumulative': url_for('static', filename=f'plots/{cum_file}')
                }

            # correlation & random
            corr_file = f"corr_{run_id}.png"
            rand_file = f"rand_{run_id}.png"
            hist_file = f"hist_{run_id}.png"
            save_fig(corr, os.path.join(PLOT_DIR, corr_file))
            save_fig(rand, os.path.join(PLOT_DIR, rand_file))
            save_fig(hist, os.path.join(PLOT_DIR, hist_file))
            viz['correlation'] = url_for('static', filename=f'plots/{corr_file}')
            viz['random'] = {
                'scatter':    url_for('static', filename=f'plots/{rand_file}'),
                'histogram':  url_for('static', filename=f'plots/{hist_file}')
            }


        # — 3. Backtesting —
        back = {}
        if do_backtest and days >= MIN_BACKTEST_DAYS:
            for name, key, _ in strategies:
                pr, cr, stats, fig = optimizer.backtest_portfolio(
                    data.index[0], data.index[-1],
                    train_window=252, rebalance_period=63,
                    optimization_method=key,
                    transaction_cost=0.001
                )
                # stats[key] is a dict of metrics
                method_stats = stats[key]
                back[name] = {
                    'Total Return':        round(method_stats['Total Return'], 2),
                    'Annualized Return':   round(method_stats['Annualized Return'], 2),
                    'Annualized Volatility': round(method_stats['Annualized Volatility'], 2),
                    'Sharpe Ratio':        round(method_stats['Sharpe Ratio'], 2),
                    'Maximum Drawdown':    round(method_stats['Maximum Drawdown'], 2)
                }

        # — 4. Sensitivity Analysis —
        sens = {}
        if do_sensitivity and days >= MIN_SENSITIVITY_DAYS:
            for name, key, _ in strategies:
                df = optimizer.sensitivity_analysis(
                    train_windows=[252, 126],
                    rebalance_periods=[63, 21],
                    optimization_method=key
                )
                sens[name] = {
                    'Train Window':         df['Train Window'],
                    'Rebalance Period':     df['Rebalance Period'],
                    'Annualized Return':    [float(f"{v:.3f}") for v in df['Annualized Return']],
                    'Annualized Volatility':[float(f"{v:.3f}") for v in df['Annualized Volatility']],
                    'Sharpe Ratio':         [float(f"{v:.3f}") for v in df['Sharpe Ratio']],
                    'Max Drawdown':         [float(f"{v:.3f}") for v in df['Max Drawdown']]
                }


        return render_template(
            'results.html',
            title='Portfolio Optimization Analysis Report',
            generated=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            opt=opt,
            viz=viz,
            back=back,
            sens=sens,
            days=days,
            min_back=MIN_BACKTEST_DAYS,
            min_sens=MIN_SENSITIVITY_DAYS
        )

    # GET → show form
    return render_template('index.html')


def get_description(key):
    return {
        'Maximum Sharpe Ratio':    'Optimizes the Sharpe ratio for best return per unit risk.',
        'Minimum Volatility':       'Minimizes portfolio volatility.',
        'Hierarchical Risk Parity': 'Clusters assets and allocates risk evenly.',
        'Equal Risk Contribution':  'Balances risk contribution among assets.',
        'Equal Weight':             'Assigns equal weight to each asset.',
        'Maximum Diversification':  'Maximizes diversification ratio.',
        'Minimum CVaR':             'Minimizes potential tail losses (CVaR).'
    }.get(key, '')


if __name__ == '__main__':
    app.run(debug=True)
