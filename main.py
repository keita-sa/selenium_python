import time

from selenium import webdriver

# Open browser
driver = webdriver.Chrome()
time.sleep(5)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10)