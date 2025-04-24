| 1 | AAPL | 
| 2 | NVDA | 
**Correlation Matrix:**  
  ![Correlation Matrix]({plots_dir}/correl_mat.png)    
# Portfolio Optimization Analysis Report

**Report generated on:** 2025-04-23 19:53:55

This report provides a comprehensive overview of various portfolio optimization techniques. For each method, we briefly explain the approach, present key performance metrics, and display supporting plots such as cumulative returns, portfolio allocations, and risk contributions. Additionally, backtesting and sensitivity analyses are structured for clarity.

---

## 1. Portfolio Optimization Methods

### Maximum Sharpe Ratio
**Description:**  
This method optimizes the portfolio by maximizing the Sharpe Ratio, seeking the best balance between returns and risk.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.53 |
| Annualized Volatility     | 0.48 |
| Weights                   |  |
| AAPL | 0.00 |
| NVDA | 1.00 |
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
This approach minimizes overall portfolio volatility, targeting lower risk even if it sacrifices some returns.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.07 |
| Annualized Volatility     | 0.26 |
| Weights                   |  |
| AAPL | 1.00 |
| NVDA | 0.00 |
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
HRP clusters assets based on correlations and allocates risk evenly among clusters, enhancing diversification.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.23 |
| Annualized Volatility     | 0.3 |
| Weights                   |  |
| AAPL | 0.65 |
| NVDA | 0.35 |
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
This method equalizes the risk contributed by each asset, ensuring no single asset dominates the portfolio’s risk.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.23 |
| Annualized Volatility     | 0.3 |
| Weights                   |  |
| AAPL | 0.65 |
| NVDA | 0.35 |
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
This technique maximizes the diversification ratio to achieve the best mix of assets for risk reduction.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.23 |
| Annualized Volatility     | 0.3 |
| Weights                   |  |
| AAPL | 0.65 |
| NVDA | 0.35 |
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
This simple strategy assigns an equal weight to each asset, serving as a baseline for comparison.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.3 |
| Annualized Volatility     | 0.33 |
| Weights                   |  |
| AAPL | 0.50 |
| NVDA | 0.50 |
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
Minimum CVaR targets the reduction of extreme losses, focusing on the tail risk of the portfolio distribution.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.3 |
| Annualized Volatility     | 0.33 |
| Weights                   |  |
| AAPL | 0.50 |
| NVDA | 0.50 |
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
| Maximum Sharpe (max_sharpe) | 3.31e-01 | 1.1879126310434878 | 0.2925402098577277 | 4.026498208968767 | -0.05014640356358677 |
| Minimum Volatility (min_vol) | 1.76e-01 | 0.6627443489452491 | 0.16987030283694374 | 3.8426042577425075 | -0.030365540703045885 |
| Hierarchical Risk Parity (HRP) | 2.54e-01 | 0.9306718485893066 | 0.21398943535624304 | 4.302417299511074 | -0.036295552842904914 |
| Equal Risk Contribution (ERC) | 2.54e-01 | 0.9307037319198814 | 0.2139976207981166 | 4.302401720570832 | -0.03629712908331649 |
| Maximum Diversification (max_div) | 2.50e-01 | 0.916182726568207 | 0.21032377825350912 | 4.308512970302196 | -0.03557917556453632 |
| Equal Weight (Eq) | 2.88e-01 | 1.0423647444349777 | 0.2454304697433223 | 4.2063430246238465 | -0.04181337742387607 |
| Minimum CVAR Contribution (min_cvar) | 2.88e-01 | 1.0423647444349777 | 0.2454304697433223 | 4.2063430246238465 | -0.04181337742387607 |

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
| max_sharpe | 252 | 63 | 1.1879126310434878 | 0.2925402098577277 | 4.026498208968767 | -0.05014640356358677 |
| max_sharpe | 252 | 21 | 0.8558835956552754 | 0.27915983950650497 | 3.030104893134403 | -0.04899151814086722 |
| max_sharpe | 126 | 63 | -0.4680386396583933 | 0.2786680938801752 | -1.7154408780789439 | -0.33214352142757164 |
| max_sharpe | 126 | 21 | 0.3713292182520021 | 0.35597620857087003 | 1.0150375490053751 | -0.17528394185931453 |
| min_vol | 252 | 63 | 0.6627443489452491 | 0.16987030283694374 | 3.8426042577425075 | -0.030365540703045885 |
| min_vol | 252 | 21 | 0.5272248946269351 | 0.2166890037498778 | 2.386945741021373 | -0.023086730026283503 |
| min_vol | 126 | 63 | -0.5054371700064577 | 0.27655493965884503 | -1.8637785701542524 | -0.3407843280375671 |
| min_vol | 126 | 21 | -0.3707107635017637 | 0.2453150555916058 | -1.551925798372364 | -0.19127159165271188 |
| HRP | 252 | 63 | 0.9306718485893066 | 0.21398943535624304 | 4.302417299511074 | -0.036295552842904914 |
| HRP | 252 | 21 | 0.6948982043153427 | 0.2318292778754695 | 2.954321432529526 | -0.036295552842904914 |
| HRP | 126 | 63 | -0.14908058569347388 | 0.3063006674481108 | -0.5193608849070599 | -0.23321424707760754 |
| HRP | 126 | 21 | 0.5113540023901818 | 0.2794348856862775 | 1.794171122044703 | -0.1049439112933992 |
| ERC | 252 | 63 | 0.9307037319198814 | 0.2139976207981166 | 4.302401720570832 | -0.03629712908331649 |
| ERC | 252 | 21 | 0.6949181574129846 | 0.2318334301784031 | 2.9543545850394333 | -0.03629712908331649 |
| ERC | 126 | 63 | -0.14897368134137037 | 0.30633205525769136 | -0.5189586875184813 | -0.23318702757517856 |
| ERC | 126 | 21 | 0.5115274780804402 | 0.27944674463971403 | 1.7947157649914696 | -0.10493884160644805 |
| Eq | 252 | 63 | 1.0423647444349777 | 0.2454304697433223 | 4.2063430246238465 | -0.04181337742387607 |
| Eq | 252 | 21 | 0.7647974029418605 | 0.24923929180109006 | 3.028404540421501 | -0.04181337742387607 |
| Eq | 126 | 63 | 0.01135600046896107 | 0.33618919868985825 | 0.004033444483777151 | -0.18771695968419783 |
| Eq | 126 | 21 | 0.905471833387089 | 0.3077766450878018 | 2.9094859784816713 | -0.07285814164148621 |
| max_div | 252 | 63 | 0.916182726568207 | 0.21032377825350912 | 4.308512970302196 | -0.03557917556453632 |
| max_div | 252 | 21 | 0.6858306802762482 | 0.2299943563558358 | 2.9384663649339147 | -0.03557917556453632 |
| max_div | 126 | 63 | -0.12741364813956674 | 0.31445095617301466 | -0.4369954851209297 | -0.23153941702069422 |
| max_div | 126 | 21 | 0.5286454533753839 | 0.27748348571772163 | 1.8691038568795821 | -0.10410508741754537 |
| min_cvar | 252 | 63 | 1.0423647444349777 | 0.2454304697433223 | 4.2063430246238465 | -0.04181337742387607 |
| min_cvar | 252 | 21 | 0.7647974029418605 | 0.24923929180109006 | 3.028404540421501 | -0.04181337742387607 |
| min_cvar | 126 | 63 | 0.01135600046896107 | 0.33618919868985825 | 0.004033444483777151 | -0.18771695968419783 |
| min_cvar | 126 | 21 | 0.905471833387089 | 0.3077766450878018 | 2.9094859784816713 | -0.07285814164148621 |


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
