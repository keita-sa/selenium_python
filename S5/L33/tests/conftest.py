import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Before the test, the code is executed up to the yield statement, and after the test, it's executed after the yield statement.
@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()