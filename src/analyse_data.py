import sqlite3
import pandas as pd

def fetch_all_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()
    return df

def query_data(start_date, end_date):
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather WHERE timestamp BETWEEN ? AND ?', conn, params=(start_date, end_date))
    conn.close()
    return df

if __name__ == '__main__':
    df = fetch_all_data()
    print(df.describe())
    
    df_filtered = query_data('2023-01-01', '2023-12-31')
    print(df_filtered)
