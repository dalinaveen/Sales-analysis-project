import pandas as pd
import sqlite3
import streamlit as st

df=pd.read_csv('cleaned_superstore.csv')
conn = sqlite3.connect('sales.db')
df.to_sql("sales",conn,if_exists="replace",index=False)
print("Converted sufully")