from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Initialize the Chrome Browser
driver = webdriver.Chrome()

try:
    # 2. Open YouTube
    driver.get("https://www.youtube.com")
    
    # 3. Wait up to 10 seconds for the search box to appear
    # YouTube uses 'search_query' as the name attribute
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))

    # 4. Type and Search
    print(f"Searching on: {driver.title}")
    search_box.send_keys("Python Web Scraping: Product Prices Explained Day 27")
    search_box.send_keys(Keys.RETURN)

    # Allow time to see the results
    time.sleep(5)

finally:
    # 5. Close the browser
    driver.quit()
    print("Automation completed successfully.")