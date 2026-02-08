# Day 51: Visualizing Data in Python | Line Plots & Bar Charts Explained
import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Electronics': [12000, 15000, 11000, 18000, 22000, 21000],
    'Fashion': [8000, 9000, 15000, 12000, 11000, 14000]
}

df = pd.DataFrame(data)

# 2. Create a Line Plot (Trend Analysis)
plt.figure(figsize=(10, 5)) # Set the size of the window
plt.plot(df['Month'], df['Electronics'], label='Electronics', marker='o', color='blue', linewidth=2)
plt.plot(df['Month'], df['Fashion'], label='Fashion', marker='s', color='orange', linestyle='--')


plt.title('Monthly Sales Trend: 2026', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (₹)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()


plt.show()

# barchart

plt.figure(figsize=(8, 5))
plt.bar(df['Month'], df['Electronics'], color='skyblue')
plt.title('Electronics Sales Comparison')
plt.show()