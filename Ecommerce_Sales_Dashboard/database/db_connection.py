import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

def get_data():
    query = "SELECT * FROM Sales"
    return pd.read_sql(query, conn)