import pandas as pd

def convert_datetime(df,date_cols):
    
    for col in date_cols:
        df[col]=pd.to_datetime(df[col])
    return df

def add_date_parts(df,date_col):
    df[date_col+'_Year']=df[date_col].dt.year
    df[date_col+"_Month"]=df[date_col].dt.month_name()

    return df

def add_revenue_metrics(df):

    df['Revenue']=df["Sales"]*df['Quantity']

    df['Profit_Margin%']=(df["Profit"]/df['Revenue'])*100
    
    df['Discount_Amount']=df['Sales']/df['Discount']

    return df



