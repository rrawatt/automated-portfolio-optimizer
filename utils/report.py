"""
Module: report.py

Purpose:
    Generates a markdown report that summarizes the results of the portfolio optimization and backtesting.
    The report includes key performance metrics, portfolio weights, and placeholders for various plots.

Functions:
    - generate_report(res, tickers):
          Creates a detailed markdown report that includes:
            * A header with the generation timestamp.
            * Sections for each portfolio optimization method, describing the approach and key metrics.
            * A table summarizing backtesting results across multiple optimization methods.
            * A sensitivity analysis section that explores the impact of varying train windows and rebalance periods.
            * A conclusion with recommendations.
          The function writes the report to a file named "report.md" and prints a confirmation message.
"""


import os
from datetime import datetime
import urllib.parse

def generate_report(res, tickers):
  plots_dir = "/plots"
  report = ""

  for i in range(1, len(tickers)+1):
     report += f"| {i} | {tickers[i]} | \n"
  
  report+="""**Correlation Matrix:**  
  ![Correlation Matrix]({plots_dir}/correl_mat.png)"""
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  def format_weights(weights):
    return f"{float(weights):.2f}"
  
  def optires(method):
    nonlocal report  # This ensures we're modifying the outer 'report'
    report += f"""**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | {res[method]['Annualized Return']} |
| Annualized Volatility     | {res[method]['Annualized Volatility']} |
| Weights                   |  |"""
    
    for i in range(len(tickers)):
      report += f"\n| {tickers[i]} | {format_weights(res[method]['Weights'][i])} |"
    
    report += f"""
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns]({plots_dir}/{urllib.parse.quote(method)}_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation]({plots_dir}/{urllib.parse.quote(method)}_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions]({plots_dir}/{urllib.parse.quote(method)}_risk_contributions.png)  

---
"""
  
  report += f"""    
# Portfolio Optimization Analysis Report

**Report generated on:** {now}

This report provides a comprehensive overview of various portfolio optimization techniques. For each method, we briefly explain the approach, present key performance metrics, and display supporting plots such as cumulative returns, portfolio allocations, and risk contributions. Additionally, backtesting and sensitivity analyses are structured for clarity.

---

## 1. Portfolio Optimization Methods

### Maximum Sharpe Ratio
**Description:**  
This method optimizes the portfolio by maximizing the Sharpe Ratio, seeking the best balance between returns and risk."""
  optires('Maximum Sharpe Ratio')

  report += f"""
### Minimum Volatility
**Description:**  
This approach minimizes overall portfolio volatility, targeting lower risk even if it sacrifices some returns."""
  optires('Minimum Volatility')

  report += f"""
### Hierarchical Risk Parity (HRP)
**Description:**  
HRP clusters assets based on correlations and allocates risk evenly among clusters, enhancing diversification."""
  optires('Hierarchical Risk Parity')

  report += f"""
### Equal Risk Contribution (ERC)
**Description:**  
This method equalizes the risk contributed by each asset, ensuring no single asset dominates the portfolio’s risk."""
  optires('Equal Risk')
  
  report += f"""
### Maximum Diversification
**Description:**  
This technique maximizes the diversification ratio to achieve the best mix of assets for risk reduction."""
  optires('Maximum Diversification')

  report += f"""
### Equal Weight
**Description:**  
This simple strategy assigns an equal weight to each asset, serving as a baseline for comparison."""
  optires('Equal Weight')

  report += f"""
### Minimum CVaR
**Description:**  
Minimum CVaR targets the reduction of extreme losses, focusing on the tail risk of the portfolio distribution."""
  optires('Minimum CVaR')
  
  report += f"""

## 2. Backtesting Results

Backtesting was performed using a rolling window (Training Window = 252 days, Rebalance Period = 63 days, Transaction Cost = 0.1%). Below are the summarized results:

| Method                  | Total Return         | Annualized Return | Annualized Volatility | Sharpe Ratio | Maximum Drawdown |
|-------------------------|----------------------|-------------------|-----------------------|--------------|------------------|
| Maximum Sharpe (max_sharpe) | {res['backtesting']['max_sharpe']['max_sharpe']['Total Return']:.2e} | {res['backtesting']['max_sharpe']['max_sharpe']['Annualized Return']} | {res['backtesting']['max_sharpe']['max_sharpe']['Annualized Volatility']} | {res['backtesting']['max_sharpe']['max_sharpe']['Sharpe Ratio']} | {res['backtesting']['max_sharpe']['max_sharpe']['Maximum Drawdown']} |
| Minimum Volatility (min_vol) | {res['backtesting']['min_vol']['min_vol']['Total Return']:.2e} | {res['backtesting']['min_vol']['min_vol']['Annualized Return']} | {res['backtesting']['min_vol']['min_vol']['Annualized Volatility']} | {res['backtesting']['min_vol']['min_vol']['Sharpe Ratio']} | {res['backtesting']['min_vol']['min_vol']['Maximum Drawdown']} |
| Hierarchical Risk Parity (HRP) | {res['backtesting']['HRP']['HRP']['Total Return']:.2e} | {res['backtesting']['HRP']['HRP']['Annualized Return']} | {res['backtesting']['HRP']['HRP']['Annualized Volatility']} | {res['backtesting']['HRP']['HRP']['Sharpe Ratio']} | {res['backtesting']['HRP']['HRP']['Maximum Drawdown']} |
| Equal Risk Contribution (ERC) | {res['backtesting']['ERC']['ERC']['Total Return']:.2e} | {res['backtesting']['ERC']['ERC']['Annualized Return']} | {res['backtesting']['ERC']['ERC']['Annualized Volatility']} | {res['backtesting']['ERC']['ERC']['Sharpe Ratio']} | {res['backtesting']['ERC']['ERC']['Maximum Drawdown']} |
| Maximum Diversification (max_div) | {res['backtesting']['max_div']['max_div']['Total Return']:.2e} | {res['backtesting']['max_div']['max_div']['Annualized Return']} | {res['backtesting']['max_div']['max_div']['Annualized Volatility']} | {res['backtesting']['max_div']['max_div']['Sharpe Ratio']} | {res['backtesting']['max_div']['max_div']['Maximum Drawdown']} |
| Equal Weight (Eq) | {res['backtesting']['Eq']['Eq']['Total Return']:.2e} | {res['backtesting']['Eq']['Eq']['Annualized Return']} | {res['backtesting']['Eq']['Eq']['Annualized Volatility']} | {res['backtesting']['Eq']['Eq']['Sharpe Ratio']} | {res['backtesting']['Eq']['Eq']['Maximum Drawdown']} |
| Minimum CVAR Contribution (min_cvar) | {res['backtesting']['min_cvar']['min_cvar']['Total Return']:.2e} | {res['backtesting']['min_cvar']['min_cvar']['Annualized Return']} | {res['backtesting']['min_cvar']['min_cvar']['Annualized Volatility']} | {res['backtesting']['min_cvar']['min_cvar']['Sharpe Ratio']} | {res['backtesting']['min_cvar']['min_cvar']['Maximum Drawdown']} |

**Backtesting Plots:**  
- **Maximum Sharpe Backtest:**  
  ![Max Sharpe Backtest]({plots_dir}/max_sharpe_backtest.png)  
- **Minimum Volatility Backtest:**  
  ![Min Vol Backtest]({plots_dir}/min_vol_backtest.png)  
- **HRP Backtest:**  
  ![HRP Backtest]({plots_dir}/HRP_backtest.png)  
- **ERC Backtest:**  
  ![ERC Backtest]({plots_dir}/ERC_backtest.png)  
- **Max div Backtest:**  
  ![Max div Backtest]({plots_dir}/max_div_backtest.png) 
- **Eq Weight Backtest:**  
  ![Eq Weight Backtest]({plots_dir}/Eq_backtest.png) 
- **Min CVAR Backtest:**  
  ![Min CVAR Backtest]({plots_dir}/min_cvar_backtest.png) 

---

## 3. Sensitivity Analysis

The sensitivity analysis explores how different parameter choices affect portfolio performance:

|Method | Train Window | Rebalance Period | Annualized Return | Annualized Volatility | Sharpe Ratio | Max Drawdown |
|-------|--------------|------------------|-------------------|-----------------------|--------------|--------------|
"""
  sens = res['Sensitivity Analysis']
  for j in sens.keys():
    for i in range(len(sens[j]["Train Window"])):
        report += f"| {j} | { sens[j]['Train Window'][i]} | { sens[j]['Rebalance Period'][i]} | { sens[j]['Annualized Return'][i]} | {sens[j]['Annualized Volatility'][i]} | {sens[j]['Sharpe Ratio'][i]} | {sens[j]['Max Drawdown'][i]} |\n"
  report += f"""

---

## 4. Conclusion and Recommendations

The analysis shows that each portfolio optimization method offers a different balance between return and risk:

- **Maximum Sharpe Ratio:** Focuses on maximizing risk-adjusted returns.
- **Minimum Volatility:** Prioritizes reducing portfolio risk.
- **Hierarchical Risk Parity (HRP):** Enhances diversification by grouping correlated assets.
- **Equal Risk Contribution (ERC):** Balances risk evenly across assets.
- **Maximum Diversification:** Seeks the best mix of assets to lower overall risk.
- **Equal Weight:** Provides a simple baseline strategy.
- **Minimum CVaR:** Targets extreme risk reduction by minimizing potential tail losses.

**Recommendations:**  
Consider blending these techniques to tailor your portfolio to your risk tolerance and return objectives. Regularly review both the backtesting and sensitivity analysis to adapt to changing market conditions.

---

**End of Report**
"""

  # Write the report to a Markdown file.
  with open("report.md", "w") as f:
      f.write(report)

  print("Report saved to report.md")
