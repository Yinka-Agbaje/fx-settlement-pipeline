import pandas as pd
from sqlalchemy import create_engine

def query_warehouse():
    engine = create_engine('sqlite:///settlement_warehouse.db')
    
    query = """
    SELECT 
        Merchant_ID, 
        Transaction_Amount, 
        Live_NGN_Rate, 
        Settlement_Amount_NGN, 
        Gateway_Revenue_NGN
    FROM daily_settlements
    ORDER BY Gateway_Revenue_NGN DESC;
    """
    
    df = pd.read_sql(query, con=engine)
    return df

if __name__ == "__main__":
    results = query_warehouse()
    print("Warehouse Query Successful. Top Revenue Generating Transactions:")
    print(results)