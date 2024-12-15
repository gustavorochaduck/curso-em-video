import pandas as pd
import sqlite3

con = sqlite3.connect("products.sql")

def show(info):
    if info == "ALL":
        read_all = pd.read_sql_query("SELECT * FROM products", con)
        print(read_all)
