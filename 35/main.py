import requests
from bs4 import BeautifulSoup

def check_price(url, target_price):
    # Headers are crucial to avoid being blocked by Amazon
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Note: Amazon's CSS classes change frequently; 
        # You may need to inspect the page and update these
        title = soup.find(id="productTitle").get_text().strip()
        price_str = soup.find(class_="a-price-whole").get_text()
        
        # Convert price string to a float
        current_price = float(price_str.replace(',', '').replace('.', ''))

        print(f"Product: {title[:50]}...")
        print(f"Current Price: ₹{current_price}")

        if current_price <= target_price:
            print("🚨 ALERT: Price dropped! Buy now!")
        else:
            print(f"Still waiting... Target is ₹{target_price}")

    except Exception as e:
        print(f"Error fetching price: {e}")

# Example Product URL
product_url = "https://www.amazon.in/dp/B0FQG1LPVF"
check_price(product_url, target_price=135000.0)