#------Import Modules--------------
import pandas as pd
from functions import *
from transform import *
import matplotlib.pyplot as plt
import seaborn as sns


#-----------Loading the CSV file ---------
df =pd.read_csv("Sample - Superstore.csv",encoding="latin-1")
#show all rows
pd.set_option('display.max_rows', None)

# Show all columns
pd.set_option('display.max_columns', None)

explore_data(df) # User define function 

missing_report(df) #Analysing Missing values

df=check_duplicate(df) #checking Duplicate records in data

#Dtype changing / Extract  / Adding columns

df = convert_datetime(df,['Order Date','Ship Date'])

df=add_date_parts(df,'Order Date')
print(df.info())

df=add_revenue_metrics(df)

#------Aggregations (project-specific)-------------
"""summarize the data for insights:

By Product: total revenue, total profit, average discount

By Customer: total revenue, total profit, number of transactions

By Region/Category: total sales, total profit """

#------------------------------------------By Product: total revenue, total profit, average discount-----------------------

Product_Summary=df.groupby(
    df['Product Name']).agg(
        Total_Revenue =("Revenue","sum"),
        Total_Profit=("Profit",'sum'),
        Average_discount=('Discount','mean')
    ).reset_index()

Product_Summary['Total_Revenue']=Product_Summary['Total_Revenue'].apply(lambda x:f'₹{x:,.2f}')
Product_Summary['Total_Profit']=Product_Summary['Total_Profit'].apply(lambda x:f'₹{x:,.2f}')

#---------------------------------------By Customer: total revenue, total profit, number of transactions------------

Customer_Summary=df.groupby(['Customer ID','Customer Name'])\
    .agg(
        Total_Revenue =("Revenue","sum"),
        Total_Profit=("Profit",'sum'),
        Average_discount=('Discount','mean')
    ).reset_index()
Customer_Summary['Total_Revenue']= Customer_Summary['Total_Revenue'].apply(lambda x: f"₹{x:,.2f}")
Customer_Summary['Total_Profit']=Customer_Summary['Total_Profit'].apply(lambda x:f'₹{x:,.2f}')


#----------------------------------By Category: total sales, total profit-----------------------------
 
Category_Summary=df.groupby('Category')\
    .agg(
         Total_Revenue =("Revenue","sum"),
        Total_Profit=("Profit",'sum'),
        Average_discount=('Discount','mean')
    ).reset_index()
#Category_Summary['Total_Revenue']=Category_Summary['Total_Revenue'].apply(lambda x:f'₹{x:,.2f}')
#Category_Summary['Total_Profit']=Category_Summary['Total_Profit'].apply(lambda x:f'₹{x:,.2f}')

print(Category_Summary.columns)
#----------------------------------------By Region :total sales, total profit ,Revenue---------

Region_Summary=df.groupby('Region')\
    .agg(Total_Revenue =("Revenue","sum"),
        Total_Profit=("Profit",'sum'),
        Average_discount=('Discount','mean')
    ).reset_index()
#Region_Summary['Total_Revenue']=Region_Summary['Total_Revenue'].apply(lambda x:f'₹{x:,.2f}')
Region_Summary['Total_Profit']=Region_Summary['Total_Profit'].apply(lambda x:f'₹{x:,.2f}')

#----------------------------By Monthly Summary on Year :total sales, total profit , Revenue------------------

Monthly_Summary=df.groupby(['Order Date_Year','Order Date_Month'])\
    .agg(Total_Revenue =("Revenue","sum"),
        Total_Profit=("Profit",'sum'),
        Average_discount=('Discount','mean')
    ).reset_index()
#Monthly_Summary['Total_Revenue']=Monthly_Summary['Total_Revenue'].apply(lambda x:f'₹{x:,.2f}')
Monthly_Summary['Total_Profit']=Monthly_Summary['Total_Profit'].apply(lambda x:f'₹{x:,.2f}')


#------------------------------------------Visualization ------------------

#-------------- Revenue by Region------

plt.figure(figsize=(8,5))
sns.barplot(x="Region",y="Total_Revenue",data=Region_Summary,palette='viridis')
plt.title("Revenue By Region")
plt.ylabel("Revenue")
plt.show()

#-------------- Revenue by Year------
plt.figure(figsize=(8,6))
sns.barplot(x='Order Date_Year',y='Total_Revenue',data=Monthly_Summary,ci=None, palette='viridis')
plt.title("Yearly Revenue")
plt.ylabel("Revenue")
plt.show()

#-------------- Revenue by Year------

plt.figure(figsize=(8,4))
sns.barplot(x='Category',y='Total_Revenue',data=Category_Summary, palette='viridis')
plt.title("Revenue By Category")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(8,4))
sns.barplot(x='Category',y='Total_Profit',data=Category_Summary, palette='viridis')
plt.title("Profit By Category")
plt.ylabel("Profit")
plt.show()

df.to_csv("cleaned_superstore.csv",index=False)
Product_Summary.to_csv("Product_Summary.csv",index=False)
Customer_Summary.to_csv('Customer_Summary.csv',index=False)
Category_Summary.to_csv('Category_Summary.csv',index=False)
Monthly_Summary.to_csv('Monthly_Summary.csv',index=False)
print("saved...")