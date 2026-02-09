import plotly.express as px
import pandas as pd
import numpy as np

# 1. Generate Interactive Data
# Creating a dataset representing 500 different store locations
np.random.seed(42)
data = {
    'Location': [f"Store {i}" for i in range(1, 501)],
    'Sales_Revenue': np.random.randint(20000, 100000, 500),
    'Customer_Count': np.random.randint(500, 5000, 500),
    'Region': np.random.choice(['North America', 'Europe', 'Asia', 'South America'], 500),
    'Profit_Margin': np.random.uniform(0.05, 0.30, 500)
}

df = pd.DataFrame(data)

# 2. Creating the Interactive Scatter Plot
# Hover over points to see details!
fig = px.scatter(
    df, 
    x="Customer_Count", 
    y="Sales_Revenue",
    size="Profit_Margin", 
    color="Region",
    hover_name="Location",
    log_x=True, 
    size_max=20,
    title="Interactive Global Sales Intelligence - Day 52",
    labels={"Customer_Count": "Number of Customers", "Sales_Revenue": "Total Revenue ($)"},
    template="plotly_dark" # Dark mode for that pro look
)

# 3. Adding Interactivity Controls
fig.update_layout(
    hovermode="closest",
    dragmode="zoom"
)

# 4. Display the dashboard in your browser
fig.show()