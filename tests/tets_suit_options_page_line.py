from tests.test_base_set_up_class import TestBaseSetUPLine


class TestOptionsPageLine(TestBaseSetUPLine):
    driver = None

    @classmethod
    def setUpClass(cls):
        """ Open site's main page,
        click button 'Options',
        select chart type as 'Line',
        apply modal window, click button 'Options'"""
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Close browser."""
        super().tearDownClass()

    def test05_data_values_after_selecting_line(self):
        """Check text field 'Data values' after
        selecting chart type as 'Line'"""
        data_value = self.options_page.text_data_value()
        self.assertEqual('Original', data_value)

    def test06_order_by_after_selecting_line(self):
        """Check text field 'Order by' after
        selecting chart type as 'Line'"""
        order_by = self.options_page.text_order_by()
        self.assertEqual('Count', order_by)

    def test07_order_direction_after_selecting_line(self):
        """Check text field 'Order_direction' after
        selecting chart type as 'Line'"""
        order_direction = self.options_page.text_order_direction()
        self.assertEqual('DESC', order_direction)

    def test08_line_width_after_selecting_line(self):
        """Check text field 'Line width' after
        selecting chart type as 'Line'"""
        line_width = self.options_page.text_line_width()
        self.assertEqual('4', line_width)
