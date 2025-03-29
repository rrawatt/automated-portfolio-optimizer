res = {
    'Maximum Sharpe Ratio': {
        'Weights': [0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667],
        'Annualized Return': 61567.52,
        'Annualized Volatility': 698.56
    },
    'Minimum Volatility': {
        'Weights': [0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667],
        'Annualized Return': 61567.52,
        'Annualized Volatility': 698.56
    },
    'Hierarchical Risk Parity': {
        'Weights': [0.07658922, 0.06570809, 0.02685701, 0.05102677, 0.2870292,
                    0.07228171, 0.12244447, 0.00696902, 0.04193864, 0.00384315,
                    0.02049347, 0.16365979, 0.0122137, 0.02746106, 0.0214847],
        'Annualized Return': 39735.89,
        'Annualized Volatility': 252.37
    },
    'Equal Risk Contribution': {
        'Weights': [0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667],
        'Annualized Return': 61567.52,
        'Annualized Volatility': 698.56
    },
    'Equal Weight': {
        'Weights': [0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667],
        'Annualized Return': 61567.52,
        'Annualized Volatility': 698.56
    },
    'Maximum Diversification': {
        'Weights': [9.76254166e-15, 2.16112274e-01, 8.47191600e-15, 1.94649883e-01,
                    7.10243143e-02, 0.00000000e+00, 4.55530070e-01, 9.18215495e-14,
                    0.00000000e+00, 1.77826417e-13, 0.00000000e+00, 0.00000000e+00,
                    4.88861384e-14, 6.26834578e-02, 2.52355737e-15],
        'Annualized Return': 34565.69,
        'Annualized Volatility': 127.73
    },
    'Minimum CVaR': {
        'Weights': [0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667,
                    0.06666667, 0.06666667, 0.06666667, 0.06666667, 0.06666667],
        'Annualized Return': 61567.52,
        'Annualized Volatility': 698.56
    },
    'backtesting': {
        'max_sharpe': {
            'max_sharpe': {
                'Total Return': 2.2310386134804948e+151,
                'Annualized Return': 63425.88,
                'Annualized Volatility': 131.62,
                'Sharpe Ratio': 481.87,
                'Maximum Drawdown': 0.0
            }
        },
        'min_vol': {
            'min_vol': {
                'Total Return': 2.2310386134804948e+151,
                'Annualized Return': 63425.88,
                'Annualized Volatility': 131.62,
                'Sharpe Ratio': 481.87,
                'Maximum Drawdown': 0.0
            }
        },
        'HRP': {
            'HRP': {
                'Total Return': 4.228946110715126e+137,
                'Annualized Return': 38302.41,
                'Annualized Volatility': 59.69,
                'Sharpe Ratio': 641.68,
                'Maximum Drawdown': 0.0
            }
        },
        'ERC': {
            'ERC': {
                'Total Return': 2.2310386134804948e+151,
                'Annualized Return': 63425.88,
                'Annualized Volatility': 131.62,
                'Sharpe Ratio': 481.87,
                'Maximum Drawdown': 0.0
            }
        }
    },
    'Sensitivity Analysis': {
        'Train Window': {0: 252, 1: 252, 2: 126, 3: 126},
        'Rebalance Period': {0: 63, 1: 21, 2: 63, 3: 21},
        'Annualized Return': {0: 63425.88, 1: 62035.1, 2: 59401.79, 3: 63760.41},
        'Annualized Volatility': {0: 131.62, 1: 93.68, 2: 498.39, 3: 774.51},
        'Sharpe Ratio': {0: 481.87, 1: 662.17, 2: 119.19, 3: 82.32},
        'Max Drawdown': {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0}
    }
}
from utils.report import generate_report
generate_report(res)