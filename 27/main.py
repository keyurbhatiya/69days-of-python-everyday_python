# Project: Scrape Live Product Prices using BeautifulSoup

import requests
from bs4 import BeautifulSoup
import re

class PriceTracker:
    def __init__(self,url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

    def fetch_data(self):
        try:
            response = requests.get(self.url,headers=self.headers)
            response.encoding = response.apparent_encoding

            if response.status_code == 200:
                return response.text
            return None
        except Exception as e:
            print(f"Connection Error : {e}")
            return None
    def parse_product(self,html):
        soup = BeautifulSoup(html,"html.parser")

        title = soup.find("h1").text.strip()

        price_raw = soup.find("p", class_="price_color").text.strip()

        prince_numeric = float(re.sub(r'[^\d.]','',price_raw))

        stock_text = soup.find("p",class_="instock availability").text.strip()

        return{
            "Name" : title,
            "Price" : prince_numeric,
            "Stock" : stock_text
        }
    
# execution

target_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

scraper = PriceTracker(target_url)
html_content = scraper.fetch_data()

if html_content:
    product_info = scraper.parse_product(html_content)

    print(f"{product_info['Name']}")
    print(f"Price : {product_info['Price']}")
    print(f"{product_info['Stock']}")

    if product_info['Price'] < 55.00:
        print("Alert : price is within your budget!")
    else:
        print("Price is high still too expensive..")

print("Day27/69 day python")