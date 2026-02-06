# How to Handle Large Datasets with Python Pandas

import pandas as pd
import numpy as np

data = {
    'Product' : np.random.choice(['Laptop','Phone','Tablet','Monitor'],100000),
    'Sales' : np.random.randint(100,1500,100000),
    'Region' : np.random.choice(['North','South','East','West'],100000),
    'Tax_rate' : 0.15
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv",index=False)
print("csv file created successfully! ")


df = pd.read_csv("sales_data.csv")

print("\n Data snapshot")
print(df.head())

print("\n Dataset Info ")
print(df.info())

print("\n Statical Summary")
print(df.describe())


df['Final_amount'] = df['Sales'] * df['Tax_rate']


hight_value_sales = df [
    (df['Product'] == 'Laptop') &
    (df['Region'] == 'North') &
    (df['Final_amount'] > 1200)
]

print(f"\n High-value Laptop Sales (North) : {len(hight_value_sales)}")

revenue_summary = df.groupby('Product') ['Final_amount'].sum()

print("\n Total Revenue Per Product ")
print(revenue_summary)
