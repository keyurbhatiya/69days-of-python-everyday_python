# Intro to Scikit-Learn: Build Your First ML Model in Python

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


np.random.seed(42)
ram = np.random.randint(4,64,100).reshape(-1,1) # feature (X)
prices = (ram * 5000) + np.random.normal(0,1000,100).reshape(-1,1) # target (Y)

X_tarin,X_test,y_train,y_test = train_test_split(ram,prices,test_size=0.2)

# tarin model
model = LinearRegression()
model.fit(X_tarin,y_train)

# make prediction
predicted_prices = model.predict(X_test)

new_laptop_ram = [[32]]
prediction = model.predict(new_laptop_ram)

print(f"Predicted for a 32GB laptop : ₹{prediction[0][0]:.2f}")

# visualizon

plt.scatter(ram,prices,color='blue',label= 'Actual Data')
plt.plot(ram,model.predict(ram),color='red',label='AI prediction Line',linewidth=2)
plt.title('AI price Prediction model - Day 61')

plt.xlabel('RAM (GB)')
plt.ylabel('Price (₹)')
plt.legend()
plt.show()