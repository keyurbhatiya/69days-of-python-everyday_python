# Day 29: Automating Login Forms with Selenium | Day 29

# libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# setup chrome

options = webdriver.ChromeOptions()

# Initialize driver

driver = webdriver.Chrome(options=options)


try:
    # open login page

    driver.get("https://the-internet.herokuapp.com/login")

    driver.maximize_window()

    # locate elements and input credentials

    time.sleep(2)

    username_filed = driver.find_element(By.ID,"username")
    password_filed = driver.find_element(By.ID,"password")

    login_button = driver.find_element(By.CSS_SELECTOR,"button.radius")

    # perfom action

    username_filed.send_keys("xyzuser")
    password_filed.send_keys("superpassword")

    print("Attempting to login..")
    login_button.click()

    # verify result
    time.sleep(2)
    success_message = driver.find_element(By.ID,"flash").text

    if "you logged into a secure area!" in success_message:
        print("sucess: login reached the secure area.")
    else:
        print("error: login failed")

finally:
    time.sleep(3)
    driver.quit()