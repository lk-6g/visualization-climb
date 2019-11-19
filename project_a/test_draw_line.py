import unittest
from btc_close_2017 import draw_line

class TestDrawLine(unittest.TestCase):
    def test_draw_line(self):
        x_data = [1, 2, 3]
        y_data = [5, 6, 4]
        title = 'test_title'
        y_legend = 'test_y_legend'
        test_line_chart = draw_line(x_data, y_data, title, y_legend)
        
        self.assertTrue(test_line_chart)
        
unittest.main()