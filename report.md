    
# Portfolio Optimization Analysis Report

**Report generated on:** 2025-03-29 19:16:18

This report provides a comprehensive overview of various portfolio optimization techniques. For each method, we briefly explain the approach, present key performance metrics, and display supporting plots such as cumulative returns, portfolio allocations, and risk contributions. Additionally, backtesting and sensitivity analyses are structured for clarity.

---

## 1. Portfolio Optimization Methods

### Maximum Sharpe Ratio
**Description:**  
This method optimizes the portfolio by maximizing the Sharpe Ratio, seeking the best balance between returns and risk.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.34 |
| Annualized Volatility     | 0.13 |
| Weights                   |  |
| AAPL | 0.00 |
| NVDA | 0.00 |
| MSFT | 0.00 |
| GOOGL | 0.00 |
| AMZN | 0.00 |
| TSLA | 0.00 |
| META | 0.00 |
| DIS | 0.08 |
| NFLX | 0.00 |
| BABA | 0.11 |
| V | 0.15 |
| JNJ | 0.22 |
| PG | 0.00 |
| SPY | 0.00 |
| AMD | 0.44 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Maximum%20Sharpe%20Ratio_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Maximum%20Sharpe%20Ratio_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Maximum%20Sharpe%20Ratio_risk_contributions.png)  

---

### Minimum Volatility
**Description:**  
This approach minimizes overall portfolio volatility, targeting lower risk even if it sacrifices some returns.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.12 |
| Annualized Volatility     | 0.09 |
| Weights                   |  |
| AAPL | 0.03 |
| NVDA | 0.00 |
| MSFT | 0.00 |
| GOOGL | 0.01 |
| AMZN | 0.02 |
| TSLA | 0.01 |
| META | 0.27 |
| DIS | 0.00 |
| NFLX | 0.00 |
| BABA | 0.00 |
| V | 0.01 |
| JNJ | 0.24 |
| PG | 0.37 |
| SPY | 0.00 |
| AMD | 0.04 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Minimum%20Volatility_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Minimum%20Volatility_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Minimum%20Volatility_risk_contributions.png)  

---

### Hierarchical Risk Parity (HRP)
**Description:**  
HRP clusters assets based on correlations and allocates risk evenly among clusters, enhancing diversification.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.18 |
| Annualized Volatility     | 0.12 |
| Weights                   |  |
| AAPL | 0.07 |
| NVDA | 0.03 |
| MSFT | 0.04 |
| GOOGL | 0.08 |
| AMZN | 0.08 |
| TSLA | 0.05 |
| META | 0.11 |
| DIS | 0.04 |
| NFLX | 0.06 |
| BABA | 0.05 |
| V | 0.03 |
| JNJ | 0.11 |
| PG | 0.11 |
| SPY | 0.03 |
| AMD | 0.11 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Hierarchical%20Risk%20Parity_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Hierarchical%20Risk%20Parity_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Hierarchical%20Risk%20Parity_risk_contributions.png)  

---

### Equal Risk Contribution (ERC)
**Description:**  
This method equalizes the risk contributed by each asset, ensuring no single asset dominates the portfolio’s risk.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.17 |
| Annualized Volatility     | 0.11 |
| Weights                   |  |
| AAPL | 0.06 |
| NVDA | 0.03 |
| MSFT | 0.04 |
| GOOGL | 0.05 |
| AMZN | 0.06 |
| TSLA | 0.05 |
| META | 0.17 |
| DIS | 0.04 |
| NFLX | 0.05 |
| BABA | 0.05 |
| V | 0.03 |
| JNJ | 0.17 |
| PG | 0.07 |
| SPY | 0.03 |
| AMD | 0.10 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Equal%20Risk_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Equal%20Risk_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Equal%20Risk_risk_contributions.png)  

---

### Maximum Diversification
**Description:**  
This technique maximizes the diversification ratio to achieve the best mix of assets for risk reduction.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.13 |
| Annualized Volatility     | 0.1 |
| Weights                   |  |
| AAPL | 0.04 |
| NVDA | 0.03 |
| MSFT | 0.00 |
| GOOGL | 0.07 |
| AMZN | 0.07 |
| TSLA | 0.03 |
| META | 0.31 |
| DIS | 0.03 |
| NFLX | 0.00 |
| BABA | 0.02 |
| V | 0.08 |
| JNJ | 0.28 |
| PG | 0.00 |
| SPY | 0.03 |
| AMD | 0.00 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Maximum%20Diversification_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Maximum%20Diversification_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Maximum%20Diversification_risk_contributions.png)  

---

### Equal Weight
**Description:**  
This simple strategy assigns an equal weight to each asset, serving as a baseline for comparison.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.23 |
| Annualized Volatility     | 0.16 |
| Weights                   |  |
| AAPL | 0.07 |
| NVDA | 0.07 |
| MSFT | 0.07 |
| GOOGL | 0.07 |
| AMZN | 0.07 |
| TSLA | 0.07 |
| META | 0.07 |
| DIS | 0.07 |
| NFLX | 0.07 |
| BABA | 0.07 |
| V | 0.07 |
| JNJ | 0.07 |
| PG | 0.07 |
| SPY | 0.07 |
| AMD | 0.07 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Equal%20Weight_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Equal%20Weight_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Equal%20Weight_risk_contributions.png)  

---

### Minimum CVaR
**Description:**  
Minimum CVaR targets the reduction of extreme losses, focusing on the tail risk of the portfolio distribution.**Key Results:*

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.23 |
| Annualized Volatility     | 0.16 |
| Weights                   |  |
| AAPL | 0.07 |
| NVDA | 0.07 |
| MSFT | 0.07 |
| GOOGL | 0.07 |
| AMZN | 0.07 |
| TSLA | 0.07 |
| META | 0.07 |
| DIS | 0.07 |
| NFLX | 0.07 |
| BABA | 0.07 |
| V | 0.07 |
| JNJ | 0.07 |
| PG | 0.07 |
| SPY | 0.07 |
| AMD | 0.07 |
**Plots:**  
- **Cumulative Returns:**  
  ![Cumulative Returns](/plots/Minimum%20CVaR_cumulative_returns.png)  
- **Portfolio Allocation:**  
  ![Portfolio Allocation](/plots/Minimum%20CVaR_portfolio_allocation.png)  
- **Risk Contributions:**  
  ![Risk Contributions](/plots/Minimum%20CVaR_risk_contributions.png)  

---


## 2. Backtesting Results

Backtesting was performed using a rolling window (Training Window = 252 days, Rebalance Period = 63 days, Transaction Cost = 0.1%). Below are the summarized results:

| Method                  | Total Return         | Annualized Return | Annualized Volatility | Sharpe Ratio | Maximum Drawdown |
|-------------------------|----------------------|-------------------|-----------------------|--------------|------------------|
| Maximum Sharpe (max_sharpe) | 1.36e-01 | 0.5229377978030401 | 0.1500032021462038 | 3.4195123201643014 | -0.034102434760047436 |
| Minimum Volatility (min_vol) | -1.46e-02 | -0.05558643594854685 | 0.08327793431535759 | -0.7875607925165816 | -0.046724102565789356 |
| Hierarchical Risk Parity (HRP) | 3.45e-02 | 0.14106655033222204 | 0.10547058541205659 | 1.2426834441106602 | -0.04760696863437413 |
| Equal Risk Contribution (ERC) | 2.23e-02 | 0.09262680685403021 | 0.09469714871273437 | 0.8725374309281501 | -0.047057264627274414 |
| Maximum Diversification (max_div) | 5.22e-03 | 0.02505543309958276 | 0.0927924735984955 | 0.16224842937937223 | -0.05482574907863536 |
| Equal Weight (Eq) | 5.73e-02 | 0.2308701676728565 | 0.12740826359092317 | 1.7335623408385559 | -0.05832703437772934 |
| Minimum CVAR Contribution (min_cvar) | 5.73e-02 | 0.2308701676728565 | 0.12740826359092317 | 1.7335623408385559 | -0.05832703437772934 |

**Backtesting Plots:**  
- **Maximum Sharpe Backtest:**  
  ![Max Sharpe Backtest](/plots/max_sharpe_backtest.png)  
- **Minimum Volatility Backtest:**  
  ![Min Vol Backtest](/plots/min_vol_backtest.png)  
- **HRP Backtest:**  
  ![HRP Backtest](/plots/HRP_backtest.png)  
- **ERC Backtest:**  
  ![ERC Backtest](/plots/ERC_backtest.png)  
- **Max div Backtest:**  
  ![Max div Backtest](/plots/max_div_backtest.png) 
- **Eq Weight Backtest:**  
  ![Eq Weight Backtest](/plots/Eq_backtest.png) 
- **Min CVAR Backtest:**  
  ![Min CVAR Backtest](/plots/min_cvar_backtest.png) 

---

## 3. Sensitivity Analysis

The sensitivity analysis explores how different parameter choices affect portfolio performance:

|Method | Train Window | Rebalance Period | Annualized Return | Annualized Volatility | Sharpe Ratio | Max Drawdown |
|-------|--------------|------------------|-------------------|-----------------------|--------------|--------------|
| max_sharpe | 252 | 63 | 0.5229377978030401 | 0.1500032021462038 | 3.4195123201643014 | -0.034102434760047436 |
| max_sharpe | 252 | 21 | -0.08299816240941735 | 0.1789270867831238 | -0.5197545216959785 | -0.034102434760047436 |
| max_sharpe | 126 | 63 | 0.40919336382425886 | 0.1992518047925865 | 2.0034617214122794 | -0.10848867849052136 |
| max_sharpe | 126 | 21 | 0.2692198054978471 | 0.1882024221005483 | 1.3773457461634435 | -0.09283295759354154 |
| min_vol | 252 | 63 | -0.05558643594854685 | 0.08327793431535759 | -0.7875607925165816 | -0.046724102565789356 |
| min_vol | 252 | 21 | -0.4347206264991298 | 0.09827171688598671 | -4.525418305402027 | -0.046724102565789356 |
| min_vol | 126 | 63 | 0.3001999349796317 | 0.09203233881100525 | 3.1532387281342187 | -0.050665687030572865 |
| min_vol | 126 | 21 | -0.22100436910083096 | 0.08966250378341992 | -2.5763765158602174 | -0.06531268959417627 |
| HRP | 252 | 63 | 0.14106655033222204 | 0.10547058541205659 | 1.2426834441106602 | -0.04760696863437413 |
| HRP | 252 | 21 | -0.4683578014426288 | 0.13108772135036612 | -3.6491427001320194 | -0.04760696863437413 |
| HRP | 126 | 63 | 0.37356246889938666 | 0.1234064493693608 | 2.946057282721332 | -0.05811284335191144 |
| HRP | 126 | 21 | 0.04505426482115921 | 0.12098724760240721 | 0.28973520363365757 | -0.05292591443329976 |
| ERC | 252 | 63 | 0.09262680685403021 | 0.09469714871273437 | 0.8725374309281501 | -0.047057264627274414 |
| ERC | 252 | 21 | -0.4902885949036741 | 0.11921032298735819 | -4.196688528028968 | -0.047057264627274414 |
| ERC | 126 | 63 | 0.3755583608257159 | 0.11725927280635459 | 3.1175219842051187 | -0.051512139408360115 |
| ERC | 126 | 21 | -0.009860282043463224 | 0.11177110903200277 | -0.177687080458124 | -0.050669752336591205 |
| Eq | 252 | 63 | 0.2308701676728565 | 0.12740826359092317 | 1.7335623408385559 | -0.05832703437772934 |
| Eq | 252 | 21 | -0.5504624719832458 | 0.1606575694877253 | -3.488553161673884 | -0.05832703437772934 |
| Eq | 126 | 63 | 0.4288171935792435 | 0.16601638929121418 | 2.5227460696340294 | -0.09663807591629481 |
| Eq | 126 | 21 | 0.1855685230283484 | 0.15356985201948756 | 1.1432486306366256 | -0.06802092849873531 |
| max_div | 252 | 63 | 0.02505543309958276 | 0.0927924735984955 | 0.16224842937937223 | -0.05482574907863536 |
| max_div | 252 | 21 | -0.44609325598883215 | 0.11903523559903266 | -3.8315819151664585 | -0.05482574907863536 |
| max_div | 126 | 63 | 0.3024157405192761 | 0.10824216897489497 | 2.7014955750479945 | -0.05219920988609021 |
| max_div | 126 | 21 | -0.16933716916126818 | 0.10218574258053527 | -1.7550116545850596 | -0.06017398626280405 |
| min_cvar | 252 | 63 | 0.2308701676728565 | 0.12740826359092317 | 1.7335623408385559 | -0.05832703437772934 |
| min_cvar | 252 | 21 | -0.5504624719832458 | 0.1606575694877253 | -3.488553161673884 | -0.05832703437772934 |
| min_cvar | 126 | 63 | 0.4288171935792435 | 0.16601638929121418 | 2.5227460696340294 | -0.09663807591629481 |
| min_cvar | 126 | 21 | 0.1855685230283484 | 0.15356985201948756 | 1.1432486306366256 | -0.06802092849873531 |


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
