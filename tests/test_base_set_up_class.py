import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from items.pages.main_page import MainPage
from items.pages.options_page import OptionPage


class TestBaseSetUPPercentage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Open site's main page,
        click button 'Options',
        select chart type as 'Area stacked',
        apply modal window, click button 'Options'"""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        cls.driver.get(PathUrl.SITE_URL)
        cls.driver.maximize_window()
        cls.main_page = MainPage(cls.driver)
        cls.main_page.options_button.click()
        cls.options_page = OptionPage(cls.driver)
        cls.options_page.select_chart_type('Area stacked')\
            .click_apply_button()\
            .options_button.click()

    @classmethod
    def tearDownClass(cls):
        """Close browser."""
        cls.driver.quit()


class TestBaseSetUPLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Open site's main page,
        click button 'Options',
        select chart type as 'Line',
        apply modal window, click button 'Options'"""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        cls.driver.get(PathUrl.SITE_URL)
        cls.driver.maximize_window()
        cls.main_page = MainPage(cls.driver)
        cls.main_page.options_button.click()
        cls.options_page = OptionPage(cls.driver)
        cls.options_page.select_chart_type('Line')\
            .click_apply_button()\
            .options_button.click()

    @classmethod
    def tearDownClass(cls):
        """Close browser."""
        cls.driver.quit()


class TestBaseSetUPRandomWords(unittest.TestCase):

    def setUp(self):
        """ Open site's main page"""
        self.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        self.driver.get(PathUrl.SITE_URL)
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        self.options_page = OptionPage(self.driver)

    def tearDown(self):
        """Close browser."""
        self.driver.quit()
