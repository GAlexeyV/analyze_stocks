import unittest
from datetime import datetime, timedelta
from app.main import get_stock_data, now, format_date

TIME_DELTA = 5 


class TestData(unittest.TestCase):

    """
    Test data extraction from DB.
    """

    def test_get_stock_data(self):

        data = get_stock_data(now() - timedelta(hours=TIME_DELTA), now(), "")

        self.assertIsNotNone(data)



class TestFormaDate(unittest.TestCase):

    """
    Test convertion time to string format.
    """

    def test_format_date(self):
        
        date_string = format_date(now())
        
        self.assertIsInstance(date_string, str)



    