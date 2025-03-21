import json
import os
import requests

def generate_insights(results: dict) -> str:
    """
    Generate insights from the portfolio optimization results using the OpenAI API via a direct HTTP request.

    Args:
        results (dict): The dictionary containing portfolio optimization results.

    Returns:
        str: Generated insights as a text string, or an error message.
    """

    prompt = (
        '''You are a seasoned financial analyst. Please analyze the following portfolio optimization results
        and provide detailed insights on performance, risk factors, diversification, and potential areas for improvement.\n\n
        Give the output in a structured markdown syntax, only the syntax, so that it can be automatically converted. Following are the placeholder for
        .png that are stored locally, efficient_frontier.png, portfolio_allocation.png, risk_contributions.png, cumulative_returns.png, correlation_matrix.png, simulate_random_portfolios.png, distribution_sharpe_ratios.png, Backtest_max_sharpe.png, Backtest_min_vol.png, Backtest_HRP.png, Backtest_ERC.png\n\n
        '''
    )
    prompt += json.dumps(results, indent=2)

    # Retrieve API token from the environment variable.
    AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
    if not AIPROXY_TOKEN:
        return "Error: API token (AIPROXY_TOKEN) is not set. Please set the environment variable."

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AIPROXY_TOKEN}"
    }
    data = {
        "model": "gpt-o3-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful financial analyst."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return json.dumps({
                "error": f"Request failed with status code {response.status_code}",
                "details": response.json()
            })
    except Exception as e:
        return f"Exception occurred while querying OpenAI API: {e}"

