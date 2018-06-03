import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver


class TestBase(unittest.TestCase):
    def setUp(self):
        """ Open Chrome browser."""
        self.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        self.driver.get(PathUrl.SITE_URL)
        self.driver.maximize_window()

    def tearDown(self):
        """Close browser."""
        self.driver.quit()
