# Portfolio Optimization and Management Framework  

This Python framework provides a modular approach to portfolio optimization, risk management, and performance evaluation. It includes various optimization techniques, risk-adjusted metrics, and visualization tools for financial portfolio analysis.  

## Features  
- **Portfolio Optimization**: Mean-Variance Optimization, Risk Parity, Minimum Variance, and more.  
- **Risk Management**: VaR, CVaR, Sharpe Ratio, and other risk-adjusted performance metrics.  
- **Backtesting**: Evaluate historical performance with benchmark comparisons.  
- **Visualization Tools**: Efficient frontier plotting, risk-return scatter plots, and asset allocation charts.  
- **Modular Design**: Easily extendable for custom optimization strategies.  

Command using csv: python main.py --data sample.csv --tickers AAPL NVDA MSFT --riskfree 0.01 --plots --backtest --sensitivity --llm

Command using tickers: python main.py --tickers AAPL NVDA MSFT --start 2020-04-12 --end 2024-04-12 --riskfree 0.01 --plots --backtest --sensitivity -llm


