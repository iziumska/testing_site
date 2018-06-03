from selenium.webdriver.common.by import By


class MainPageLocators(object):
    OPTIONS_BUTTON = \
        (By.CSS_SELECTOR, 'g.highcharts-button:nth-child(12)')
    TABLE_LINES = (By.CLASS_NAME, 'word-toggle-span')
    TERM = (By.CSS_SELECTOR, '.t-w-b-set>span>span:nth-child(4)')


class OptionsPageLocators(object):
    OPEN_CHART_TYPE_LIST = (By.XPATH, '//*[@id="chart_type"]')
    CHART_TYPE_LIST = (By.TAG_NAME, 'option')
    APPLY_BUTTON = (By.ID, 'apply')
    DATA_VALUE = (By.CSS_SELECTOR, '#data_values')
    ORDER_BY = (By.XPATH, '//*[@id="order_field"]')
    ORDER_DIRECTION = (By.XPATH, '//*[@id="order_direction"]')
    LINE_WIDTH = (By.XPATH, '//*[@id="line_width"]')
    SEARCH_FORM = (By.XPATH, '//*[@id="words_names"]')

