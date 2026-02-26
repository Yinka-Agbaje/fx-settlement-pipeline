from sqlalchemy import create_engine
from transformer import process_settlements

def load_to_warehouse():
    print("Initiating ETL Pipeline...")
    
    # 1. Extract & Transform (Automatically triggered)
    settlement_data = process_settlements()
    
    # 2. Establish Database Connection 
    # In production, this URL would point to a secure cloud PostgreSQL server
    engine = create_engine('sqlite:///settlement_warehouse.db')
    
    # 3. Load Data into the Warehouse
    # 'append' ensures we add today's records without deleting yesterday's
    settlement_data.to_sql('daily_settlements', con=engine, if_exists='append', index=False)
    
    print(f"Pipeline Success: Loaded {len(settlement_data)} merchant settlement records into the database.")

if __name__ == "__main__":
    load_to_warehouse()