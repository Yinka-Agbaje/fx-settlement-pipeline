import pandas as pd
from extractor import fetch_exchange_rates

def process_settlements():
    fx_rates = fetch_exchange_rates()
    
    ngn_rate_row = fx_rates.loc[fx_rates['Currency'] == 'NGN']
    if ngn_rate_row.empty:
        raise ValueError("NGN rate not found in API response.")
        
    base_ngn_rate = ngn_rate_row.iloc[0]['Exchange_Rate']
    
    transactions = pd.DataFrame({
        "Merchant_ID": ["M_001", "M_002", "M_003", "M_004"],
        "Transaction_Currency": ["USD", "USD", "USD", "USD"],
        "Transaction_Amount": [450.00, 1250.50, 89.99, 5000.00]
    })
    
    fx_spread = 0.015
    effective_rate = base_ngn_rate * (1 - fx_spread)
    
    transactions["Live_NGN_Rate"] = base_ngn_rate
    transactions["Effective_Rate"] = effective_rate
    transactions["Settlement_Amount_NGN"] = transactions["Transaction_Amount"] * effective_rate
    transactions["Gateway_Revenue_NGN"] = transactions["Transaction_Amount"] * (base_ngn_rate - effective_rate)
    transactions["Processing_Timestamp"] = pd.Timestamp.now('UTC')
    
    return transactions

if __name__ == "__main__":
    settlement_data = process_settlements()
    print("Transformation Complete. Daily Settlement Ledger:")
    print(settlement_data)