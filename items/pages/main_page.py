import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from items.pages.base_page import BasePage
from items.locators.locators import MainPageLocators
from selenium.webdriver.common.by import By


TIME_TO_WAIT = 60


class MainPage(BasePage):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        MainPage.driver = driver
        self.options_button = WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'g.highcharts-button:nth-child(12)')))

    def list_of_terms(self):
        text_list_of_terms = []
        list_of_terms = \
            WebDriverWait(self.driver, 60).until(lambda driver: self.driver.
                                                 find_elements(*MainPageLocators.TERM))
        for term in list_of_terms:
            text_list_of_terms.append(term.text)
        return text_list_of_terms

    def deleting_item_header(self):
        input_list = self.list_of_terms()
        input_list.remove('Term')
        return list(filter(None, input_list))

    def list_random_items(self):
        input_list = self.deleting_item_header()
        list_random_items = random.sample(input_list, 5)
        return list_random_items
