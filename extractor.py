import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
BASE_CURRENCY = "USD"
TARGET_CURRENCIES = ["NGN", "GBP", "EUR", "ZAR", "KES"]
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"

def fetch_exchange_rates():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    rates = data.get("conversion_rates", {})
    
    filtered_rates = {currency: rates.get(currency) for currency in TARGET_CURRENCIES if currency in rates}
    filtered_rates[BASE_CURRENCY] = 1.0 
    
    df = pd.DataFrame(list(filtered_rates.items()), columns=["Currency", "Exchange_Rate"])
    df["Timestamp"] = pd.Timestamp.now('UTC')
    
    return df

if __name__ == "__main__":
    fx_data = fetch_exchange_rates()
    print("Extraction Successful. Current Market Rates:")
    print(fx_data)