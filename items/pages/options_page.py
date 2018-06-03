from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from items.pages.base_page import BasePage
from items.pages.main_page import MainPage
from items.locators.locators import OptionsPageLocators


TIME_TO_WAIT = 30


class OptionPage(BasePage):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        OptionPage.driver = driver
        self.apply_button = \
            WebDriverWait(self.driver, 60).\
                until(lambda driver: self.driver.
                      find_element(*OptionsPageLocators.APPLY_BUTTON))

    def select_chart_type(self, require_type):
        self.driver.find_element(*OptionsPageLocators.
                                 OPEN_CHART_TYPE_LIST).click()
        types_list = self.driver.\
            find_elements(*OptionsPageLocators.CHART_TYPE_LIST)
        for chart_type in types_list:
            if chart_type.text == require_type:
                chart_type.click()
        return self

    def text_data_value(self):
        selected_option = \
            Select(self.driver.
                   find_element(By.CSS_SELECTOR, '#data_values'))
        return selected_option.first_selected_option.text

    def text_order_by(self):
        selected_option = \
            Select(self.driver.
                   find_element(By.XPATH, '//*[@id="order_field"]'))
        return selected_option.first_selected_option.text

    def text_order_direction(self):
        selected_option = \
            Select(self.driver.
                   find_element(By.XPATH, '//*[@id="order_direction"]'))
        return selected_option.first_selected_option.text

    def text_line_width(self):
        return self.driver.\
            find_element(*OptionsPageLocators.LINE_WIDTH).\
            get_attribute('value')

    def input_words_for_search(self, words):
        text_area = \
            self.driver.find_element(*OptionsPageLocators.SEARCH_FORM)
        text_area.click()
        for word in words:
            text_area.send_keys(word + ', ')
        return self

    def click_apply_button(self):
        self.apply_button.click()
        return MainPage(self.driver)
