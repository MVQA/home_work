from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from MainPage import SearchHelper

def test_open_serp_new(driver):
    cian_main_page = SearchHelper(driver)
    cian_main_page.go_to_site()
    assert "ЦИАН" in driver.title
    cian_main_page.enter_word("город Санкт-Петербург")
    cian_main_page.click_on_the_suggest_item()
    cian_main_page.click_on_the_search_button()
    cian_main_page.wait_title("Санкт-Петербург")
    assert "Санкт-Петербург" in driver.title
    assert "Продажа 1-комн и 2-комн квартир в Санкт-Петербурге" in driver.page_source