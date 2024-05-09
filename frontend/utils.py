import pandas as pd

# Example utility functions for fetching data (mock data for demonstration)
def get_accounts():
    return [
        {"name": "Checking", "balance": 1000.0, "currency": "CAD"},
        {"name": "Savings", "balance": 5000.0, "currency": "CAD"},
        {"name": "Wallet", "balance": 10.0, "currency": "ETH"},
    ]

def get_transactions():
    return pd.DataFrame([
        {"date": "2023-01-01", "description": "Grocery", "amount": -50.0, "type": "Withdrawal"},
        {"date": "2023-01-02", "description": "Salary", "amount": 2000.0, "type": "Deposit"},
        {"date": "2023-01-03", "description": "Restaurant", "amount": -100.0, "type": "Withdrawal"},
    ])