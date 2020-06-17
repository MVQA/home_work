from BaseMain import BasePage
from selenium.webdriver.common.by import By

class CianMainLocators:
    LOCATOR_GEO_SUGGEST_FIELD = (By.XPATH, '//input[@id="geo-suggest-input"]')
    LOCATOR_SUGGEST_ITEM      = (By.XPATH, '//*[@class="geosuggest_widget-relative-4Loem7Wf"]')
    LOCATOR_SEARCH_BUTTON     = (By.XPATH, '//a[@data-mark="FiltersSearchButton"]')

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(CianMainLocators.LOCATOR_GEO_SUGGEST_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_suggest_item(self):
        return self.find_element(CianMainLocators.LOCATOR_SUGGEST_ITEM,time=10).click()

    def click_on_the_search_button(self):
        return self.find_element(CianMainLocators.LOCATOR_SEARCH_BUTTON,time=10).click()
