import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("cleaned_superstore.csv")
Customer_Summary=pd.read_csv('Customer_Summary.csv')
Product_Summary=pd.read_csv('Product_Summary.csv')
Category_Summary=pd.read_csv('Category_Summary.csv')
Monthly_Summary=pd.read_csv('Monthly_Summary.csv')

st.set_page_config(page_title="SuperStore Dashboard",layout='wide')
st.title("Superstore Dashboard")

kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric("💰 Total_Revenue", f"${df['Revenue'].sum():,.2f}")
with kpi2:
    st.metric("📦 Total Orders", f"{df['Order ID'].nunique():,}")
with kpi3:
    st.metric("📈 Profit_Margin%", f"{(df['Profit'].sum()/df['Revenue'].sum())*100:.2f}%")

col1,col2,col3=st.columns([1,1,1])

with col1:
    st.subheader("📊 Yearly Revenue\n")
    df["Order Date"]=pd.to_datetime(df['Order Date'])
    df['Year']=df["Order Date"].dt.year
    yearly_revenue=df.groupby('Year')['Revenue'].sum()
    fig, ax1 = plt.subplots(figsize=(9,7))
    yearly_revenue.plot(kind="bar", ax=ax1, color="skyblue")
    ax1.set_title("Yearly Revenue")
    ax1.set_ylabel("Revenue")
    st.pyplot(fig)
    st.write(yearly_revenue)
   


with col2:
    st.subheader("📊 Top 10 Customers by Revenue")
    top_customers = df.groupby("Customer Name")["Revenue"].sum().sort_values(ascending=False).head(10)
    fig1, ax1 = plt.subplots(figsize=(6,4))
    top_customers.plot(kind="bar", ax=ax1, color="skyblue")
    st.pyplot(fig1)
    st.write(top_customers)

with col3:
    st.subheader("🔥 Top 10 Products by Profit")
    top_products=df.groupby('Sub-Category')['Revenue'].sum().sort_values(ascending=False)
    st.bar_chart(top_products)
    st.write(top_products)

st.subheader('State revenue')
state_revenue=df.groupby('State')['Revenue'].sum().sort_values(ascending=False).head(5)
st.bar_chart(state_revenue)