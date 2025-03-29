import numpy as np
import plotly.express as px
import plotly.graph_objects as go

class VisualizationMixin:
    def plot_efficient_frontier(self, num_portfolios=1000):
        """Plot the efficient frontier by simulating random portfolios using Plotly."""
        results = np.zeros((3, num_portfolios))
        for i in range(num_portfolios):
            w = np.random.random(self.num_assets)
            w /= np.sum(w)
            ret, vol = self.calculate_portfolio_performance(w)
            results[0, i] = ret
            results[1, i] = vol
            results[2, i] = self.calculate_sharpe_ratio(w)
        
        fig = px.scatter(
            x=results[1, :], 
            y=results[0, :], 
            color=results[2, :], 
            labels={'x': 'Annualized Volatility', 'y': 'Annualized Return', 'color': 'Sharpe Ratio'},
            title="Efficient Frontier"
        )
        return fig

    def plot_portfolio_allocation(self):
        """Plot the current portfolio allocation as a bar chart using Plotly."""
        figlist={}
        if self.weight_list is None:
            print("Run an optimization method first to get weights.")
            return
        for weights in self.weight_list:
            assets = self.returns.columns.tolist()
            fig = px.bar(
                x=assets, 
                y=self.weight_list[weights], 
                labels={'x': 'Assets', 'y': 'Weight'},
                title="Portfolio Allocation"
            )
            figlist[weights]=fig
        return figlist

    def plot_risk_contributions(self):
        """Plot the risk contributions of each asset using Plotly."""
        figlist={}
        if self.weight_list is None:
            print("Run an optimization method first to get weights.")
            return
        for weights in self.weight_list:
            risk_contrib = self._calculate_risk_contributions(self.weight_list[weights])
            assets = self.returns.columns.tolist()
            fig = px.bar(
                x=assets, 
                y=risk_contrib, 
                labels={'x': 'Assets', 'y': 'Risk Contribution'},
                title="Risk Contributions"
            )
            figlist[weights]=fig
        return figlist

    def plot_cumulative_returns(self):
        """Plot cumulative portfolio returns over time using Plotly."""
        figlist={}
        if self.weight_list is None:
            print("Run an optimization method first to get weights.")
            return
        for weights in self.weight_list:
            port_returns = self.returns @ self.weight_list[weights]
            cum_returns = np.cumprod(1 + port_returns) - 1
            
            fig = px.line(
                x=self.returns.index, 
                y=cum_returns, 
                labels={'x': 'Time', 'y': 'Cumulative Return'},
                title="Cumulative Portfolio Returns"
            )
            figlist[weights]=fig
        return figlist

    def plot_correlation_matrix(self):
        """Plot a heatmap of the asset return correlation matrix using Plotly."""
        corr = self.returns.corr()
        
        fig = px.imshow(
            corr, 
            labels=dict(color="Correlation"),
            x=corr.columns,
            y=corr.columns,
            title="Correlation Matrix"
        )
        return fig

    def simulate_random_portfolios(self, num_portfolios=5000):
        """Simulate random portfolios and plot their risk-return distribution using Plotly."""
        results = np.zeros((3, num_portfolios))
        weight_records = []
        for i in range(num_portfolios):
            w = np.random.random(self.num_assets)
            w /= np.sum(w)
            weight_records.append(w)
            ret, vol = self.calculate_portfolio_performance(w)
            results[0, i] = ret
            results[1, i] = vol
            results[2, i] = self.calculate_sharpe_ratio(w)
        
        scatter_fig = px.scatter(
            x=results[1, :], 
            y=results[0, :], 
            color=results[2, :], 
            labels={'x': 'Annualized Volatility', 'y': 'Annualized Return', 'color': 'Sharpe Ratio'},
            title="Random Portfolios Simulation"
        )
        
        hist_fig = px.histogram(
            x=results[2, :], 
            nbins=50, 
            labels={'x': 'Sharpe Ratio', 'y': 'Frequency'},
            title="Distribution of Sharpe Ratios"
        )
        
        return scatter_fig, hist_fig

