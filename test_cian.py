from time import sleep
def test_open_serp(driver):
    driver.get("http://www.cian.ru")
    assert "ЦИАН" in driver.title
    elem = driver.find_element_by_xpath('//input[@id="geo-suggest-input"]')
    elem.send_keys("город Санкт-Петербург")
    sleep(2)
    clck = driver.find_element_by_xpath('//*[@class="geosuggest_widget-relative-4Loem7Wf"]')
    clck.click()
    clck = driver.find_element_by_xpath('//a[@data-mark="FiltersSearchButton"]')
    clck.click()
    sleep(1)
    assert "Санкт-Петербург" in driver.title
    driver.close()
