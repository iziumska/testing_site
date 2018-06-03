from tests.test_base_set_up_class import TestBaseSetUPPercentage


class TestOptionsPagePercentage(TestBaseSetUPPercentage):
    driver = None

    @classmethod
    def setUpClass(cls):
        """ Open site's main page,
        click button 'Options',
        select chart type as 'Area stacked',
        apply modal window, click button 'Options'"""
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Close browser."""
        super().tearDownClass()

    def test01_data_values_after_selecting_area_stacked(self):
        """Check text field 'Data values' after
        selecting chart type as 'Area stacked'"""
        data_value = self.options_page.text_data_value()
        self.assertEqual('Percentage', data_value)

    def test02_order_by_after_selecting_area_stacked(self):
        """Check text field 'Order by' after
        selecting chart type as 'Area stacked'"""
        order_by = self.options_page.text_order_by()
        self.assertEqual('Name', order_by)

    def test03_order_direction_after_selecting_area_stacked(self):
        """Check text field 'Order_direction' after
        selecting chart type as 'Area stacked'"""
        order_direction = self.options_page.text_order_direction()
        self.assertEqual('ASC', order_direction)

    def test04_line_width_after_selecting_area_stacked(self):
        """Check text field 'Line width' after
        selecting chart type as 'Area stacked'"""
        line_width = self.options_page.text_line_width()
        self.assertEqual('1', line_width)
