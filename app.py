import streamlit as st
import pandas as pd
import sqlite3

conn=sqlite3.connect('sales.db')

st.title("📊 Sales Dashboard (SQL + Streamlit)")
df=pd.read_sql('Select * from sales',conn)
st.subheader("all Sales data")
st.dataframe(df)

category = st.selectbox("Select Category",df['Category'].unique())
query = "SELECT * FROM sales WHERE Category=?"
filtered_df = pd.read_sql(query, conn, params=(category,))
st.subheader(f"Sales for {category}")
st.dataframe(filtered_df)
sales_by_cat = df.groupby("Category")["Sales"].sum().reset_index()
st.bar_chart(data=sales_by_cat, x="Category", y="Sales")

