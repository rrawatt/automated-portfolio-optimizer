| 1 | AAPL | 
| 2 | NVDA | 
| 3 | MSFT | 
**Correlation Matrix:**  
  ![Correlation Matrix]({plots_dir}/correl_mat.png)    
# Portfolio Optimization Analysis Report

**Report generated on:** 2025-04-24 10:27:50

This report provides a comprehensive overview of various portfolio optimization techniques. For each method, we briefly explain the approach, present key performance metrics, and display supporting plots such as cumulative returns, portfolio allocations, and risk contributions. Additionally, backtesting and sensitivity analyses are structured for clarity.

---

## 1. Portfolio Optimization Methods

### Maximum Sharpe Ratio
**Description:**  
This method optimizes the portfolio by maximizing the Sharpe Ratio, seeking the best balance between returns and risk.**Key Results:**

| Metric                    | Value      |
|---------------------------|------------|
| Annualized Return         | 0.44 |
| Annualized Volatility     | 0.33 |
| Weights                   |  |
| AAPL | 0.28 |
| NVDA | 0.22 |
| MSFT | 0.50 |
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
| Annualized Return         | 0.28 |
| Annualized Volatility     | 0.24 |
| Weights                   |  |
| AAPL | 0.44 |
| NVDA | 0.56 |
| MSFT | 0.00 |
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
| Annualized Return         | 0.39 |
| Annualized Volatility     | 0.29 |
| Weights                   |  |
| AAPL | 0.33 |
| NVDA | 0.34 |
| MSFT | 0.34 |
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
| Annualized Return         | 0.35 |
| Annualized Volatility     | 0.27 |
| Weights                   |  |
| AAPL | 0.39 |
| NVDA | 0.39 |
| MSFT | 0.22 |
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
| Annualized Return         | 0.36 |
| Annualized Volatility     | 0.27 |
| Weights                   |  |
| AAPL | 0.41 |
| NVDA | 0.35 |
| MSFT | 0.24 |
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
| Annualized Return         | 0.39 |
| Annualized Volatility     | 0.29 |
| Weights                   |  |
| AAPL | 0.33 |
| NVDA | 0.33 |
| MSFT | 0.33 |
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
| Annualized Return         | 0.39 |
| Annualized Volatility     | 0.29 |
| Weights                   |  |
| AAPL | 0.33 |
| NVDA | 0.33 |
| MSFT | 0.33 |
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
| Maximum Sharpe (max_sharpe) | 3.25e-01 | 0.4161904883667926 | 0.2869993193945056 | 1.4153012251866992 | -0.2724124932791059 |
| Minimum Volatility (min_vol) | 1.38e-01 | 0.19314875985452618 | 0.2064996504824236 | 0.8869204351031821 | -0.20570995553619567 |
| Hierarchical Risk Parity (HRP) | 2.54e-01 | 0.33107734463655597 | 0.24202587484956964 | 1.3266240431363816 | -0.2454834861694884 |
| Equal Risk Contribution (ERC) | 1.85e-01 | 0.25349858651689683 | 0.23399759194982855 | 1.0406029587223504 | -0.2511709202890502 |
| Maximum Diversification (max_div) | 1.43e-01 | 0.20869709885404059 | 0.24769520518440785 | 0.8021838723366146 | -0.26995465213713926 |
| Equal Weight (Eq) | 1.94e-01 | 0.2694753793667128 | 0.25592737748633543 | 1.01386331511394 | -0.27971484458330553 |
| Minimum CVAR Contribution (min_cvar) | 1.94e-01 | 0.2694753793667128 | 0.25592737748633543 | 1.01386331511394 | -0.27971484458330553 |

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
| max_sharpe | 252 | 63 | 0.41643272817626714 | 0.2871895942592101 | 1.415207014114276 | -0.2725856481644181 |
| max_sharpe | 252 | 21 | 0.057778789317722366 | 0.33223718042766937 | 0.143809278829719 | -0.11722945149686606 |
| max_sharpe | 126 | 63 | 0.5646931497748292 | 0.34419036306536144 | 1.6115882642231139 | -0.18551054371142792 |
| max_sharpe | 126 | 21 | 0.43738702676678287 | 0.3045477920669147 | 1.4033496150675693 | -0.14603892550223582 |
| min_vol | 252 | 63 | 0.19313875902820263 | 0.20653531397852662 | 0.8867188641998698 | -0.205756436392855 |
| min_vol | 252 | 21 | -0.20563537528776268 | 0.25261643591103244 | -0.8536078601144784 | -0.10883106730229793 |
| min_vol | 126 | 63 | 0.29070248573448493 | 0.24623628310058396 | 1.1399720715400095 | -0.15447965119261262 |
| min_vol | 126 | 21 | 0.3867043096738832 | 0.24453552580460164 | 1.5404890902227935 | -0.0910824113439288 |
| HRP | 252 | 63 | 0.33110548753728797 | 0.24207539859718924 | 1.3264688993514946 | -0.24554671224023492 |
| HRP | 252 | 21 | -0.14810872831184657 | 0.2955762168324732 | -0.5349169496998452 | -0.12911050859852977 |
| HRP | 126 | 63 | 0.3285248785521346 | 0.2802852619497672 | 1.1364310643248188 | -0.19652221370609363 |
| HRP | 126 | 21 | 0.4939261569167744 | 0.28552205105080414 | 1.694881901890889 | -0.1012583962808494 |
| ERC | 252 | 63 | 0.25349761432938395 | 0.23400632339910463 | 1.0405599762964168 | -0.2511825024040997 |
| ERC | 252 | 21 | -0.1597435188763091 | 0.2888044052402473 | -0.587745601508761 | -0.12021395570114132 |
| ERC | 126 | 63 | 0.28214226774065343 | 0.2717693087670909 | 1.0013723366161342 | -0.20532798757465703 |
| ERC | 126 | 21 | 0.43795150793220794 | 0.2702735748166121 | 1.5834012193851528 | -0.09897144098070193 |
| Eq | 252 | 63 | 0.2694753793667128 | 0.25592737748633543 | 1.01386331511394 | -0.27971484458330553 |
| Eq | 252 | 21 | -0.11612639728246382 | 0.31725332221627467 | -0.3975573727687625 | -0.12624387158737918 |
| Eq | 126 | 63 | 0.2724963085887526 | 0.295298324597303 | 0.8889190581989168 | -0.23361416103628954 |
| Eq | 126 | 21 | 0.4742674936182769 | 0.2917879665010584 | 1.5911125437607545 | -0.10078647580693609 |
| max_div | 252 | 63 | 0.2086875762771133 | 0.24775603004829125 | 0.801948498441738 | -0.2700302789056087 |
| max_div | 252 | 21 | -0.1075558895030879 | 0.31436165641887803 | -0.37395110727641667 | -0.11229511909846361 |
| max_div | 126 | 63 | 0.2376235781755977 | 0.30038396841881093 | 0.757775387860357 | -0.2709857708172567 |
| max_div | 126 | 21 | 0.33645847851153043 | 0.28772063351501853 | 1.1346370071665015 | -0.09875066664080313 |
| min_cvar | 252 | 63 | 0.2694753793667128 | 0.25592737748633543 | 1.01386331511394 | -0.27971484458330553 |
| min_cvar | 252 | 21 | -0.11612639728246382 | 0.31725332221627467 | -0.3975573727687625 | -0.12624387158737918 |
| min_cvar | 126 | 63 | 0.2724963085887526 | 0.295298324597303 | 0.8889190581989168 | -0.23361416103628954 |
| min_cvar | 126 | 21 | 0.4742674936182769 | 0.2917879665010584 | 1.5911125437607545 | -0.10078647580693609 |


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
