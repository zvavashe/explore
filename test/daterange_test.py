import unittest
from datetime import date

from daterange import DateRange

class TestDateRange(unittest.TestCase):
    """
    Test the functionality by the DateRange utility class.
    """
    def setUp(self):
        start_date = date(2012, 1, 1)
        end_date = date(2012, 3, 31)
        self.date_range = DateRange(start_date, end_date)
        
    def test_days_count(self):
        self.assertTrue(self.date_range.days_count() == 91, 
                        "Failed to calculate number of days in date range.")
        
    def test_includes(self):
        self.assertTrue(self.date_range.includes(date(2012, 1, 1)), 
                        "Range includes date.")
        self.assertFalse(self.date_range.includes(date(2011, 12, 31)), 
                         "Range does not include date.")
    
    def test_overlaps(self):
        other = DateRange(date(2011, 10, 1), date(2012, 1, 1))
        self.assertTrue(self.date_range.overlaps(other), 
                        "Ranges overlap by one day.")
        other = DateRange(date(2011, 10, 1), date(2012, 12, 31))
        self.assertFalse(self.date_range.overlaps(other), 
                         "Ranges do not overlap.")
        other = DateRange(date(2012, 1, 1), date(2012, 3, 31))
        self.assertTrue(self.date_range.overlaps(other), 
                        "Ranges overlap by one day.")
        
    def test_overlap(self):
        other = DateRange(date(2011, 10, 1), date(2012, 1, 1))
        self.assertTrue(self.date_range.overlap(other) == 1, 
                        "Ranges overlap by one day.")
        other = DateRange(date(2012, 2, 1), date(2012, 2, 25))
        self.assertTrue(self.date_range.overlap(other) == 25, 
                        "Ranges overlap by 25 days.")
        