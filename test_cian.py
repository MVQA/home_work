from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_open_serp(driver):
    driver.get("http://www.cian.ru")
    assert "ЦИАН" in driver.title
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="geo-suggest-input"]')))
    elem = driver.find_element_by_xpath('//input[@id="geo-suggest-input"]')
    elem.send_keys("город Санкт-Петербург")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="geosuggest_widget-relative-4Loem7Wf"]')))
    clck = driver.find_element_by_xpath('//*[@class="geosuggest_widget-relative-4Loem7Wf"]')
    clck.click()
    clck = driver.find_element_by_xpath('//a[@data-mark="FiltersSearchButton"]')
    clck.click()
    wait.until(EC.title_contains("Санкт-Петербург"))
    assert "Санкт-Петербург" in driver.title
