from tests.test_base_set_up_class import TestBaseSetUPRandomWords


class TestOptionsPageRandomWords(TestBaseSetUPRandomWords):
    driver = None

    def setUp(self):
        """ Open site's main page"""
        super().setUp()

    def tearDown(self):
        """Close browser."""
        super().tearDown()

    def test09_terms_after_input_random_terms(self):
        """Checking the information input with five random values"""
        list_random_items = self.main_page.list_random_items()
        print(list_random_items)
        self.main_page.options_button.click()
        self.options_page.input_words_for_search(list_random_items).click_apply_button()
        new_list = self.main_page.deleting_item_header()
        length_new_list = len(new_list)
        print(new_list)
        print(length_new_list)
        self.assertTrue(length_new_list == 5)
