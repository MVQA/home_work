import pytest
from selenium import webdriver
from helpers import CHROME_DRIVER_PATH

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    yield driver
    driver.quit()
