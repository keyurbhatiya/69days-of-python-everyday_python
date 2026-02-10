# Analyze Any stock with few lines of python code

# pip install yfinance matplotlib

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

ticker = "AAPL"
print(f"Fetching data for {ticker}...")

stock_data = yf.download(ticker,start="2026-01-01",end="2026-02-09")

stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()

plt.figure(figsize=(12,6))
plt.plot(stock_data['Close'],label = f'{ticker} Close price',color='blue',alpha=0.5)
plt.plot(stock_data['SMA_50'],label = '50-day SMA',color='orange',linewidth=2)


current_price = float(stock_data['Close'].iloc[-1].iloc[0] if isinstance(stock_data['Close'].iloc[-1],pd.Series)else stock_data['Close'].iloc[-1])
SMA_50 = float(stock_data['SMA_50'].iloc[-1].iloc[0] if isinstance(stock_data['SMA_50'].iloc[-1],pd.Series)else stock_data['SMA_50'].iloc[-1])

print(f"\n Current Price: {current_price:.2f}")

if current_price > SMA_50:
    print(" Trend Status : Bullish(Uptrend)")
else:
    print("Trend Status : Bearish(Downtrend)")

plt.title(f"{ticker} stock Analysis")

plt.legend()
plt.show()