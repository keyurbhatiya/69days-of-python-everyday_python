# web scraping in python

# pip install requests beautifulsoup4 

import requests
from bs4 import BeautifulSoup
from typing import List

def fetch_page(url : str) -> BeautifulSoup:
    headers = {
        "user-Agent" : "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers,timeout=10)
    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")

def extract_titles(soup:BeautifulSoup) -> List[str]:

    title = []

    for tag in soup.find_all("h2"):
        text = tag.get_text(strip=True)

        if text:
            title.append(text)
    return title

def main():
    url = "https://indianexpress.com/section/india/"
    print("Fetching website data....\n")

    soup = fetch_page(url)

    print("Extracting titles...\n")

    title = extract_titles(soup)

    if not title:
        print("No titles found.")
        return
    
    for index,title in enumerate(title,start=1):
        print(f"{index}. {title}")

print("\n Scrapping completed sucessfully..")

if __name__ == "__main__":
    main()
    print("End Day26/69 day of python")