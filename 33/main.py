import requests
import time
from datetime import datetime

def get_crypto_prices(coins):
    # CoinGecko Simple Price API
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(coins),
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        print(f"\n--- Live Update: {datetime.now().strftime('%H:%M:%S')} ---")
        for coin in coins:
            price = data[coin]['usd']
            change = data[coin]['usd_24h_change']
            emoji = "📈" if change > 0 else "📉"
            print(f"{coin.capitalize()}: ${price:,} ({emoji} {change:.2f}%)")
            
    except Exception as e:
        print(f"Connection Error: {e}")

# List of coins to track (use CoinGecko IDs)
watchlist = ['bitcoin', 'ethereum', 'dogecoin']

print("Starting Live Crypto Tracker... (Press Ctrl+C to stop)")
while True:
    get_crypto_prices(watchlist)
    time.sleep(30) # Wait 30 seconds before next update