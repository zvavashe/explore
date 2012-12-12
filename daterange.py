"""
This module includes classes that provide utility methods required when working
with date ranges.
"""

from datetime import timedelta

class DateRange(object):
    """
    A date range is a period with a start date and end date.
    """

    def __init__(self, start_date, end_date):
        """
        Creates a date range with the given start_date and end_date. Assumes
        that end_date >= start_date. This class does not support open-ended
        date ranges, that is date ranges without a specified end date.
        """
        self.start_date = start_date
        self.end_date = end_date
        
    def days_count(self):
        """
        Returns the number of days in this date range.
        """
        days = ((self.end_date - self.start_date) + timedelta(days=1)).days
        return days
    
    def includes(self, date):
        """
        Checks whether a date falls within this range. Returns true if the date
        fall within the range; otherwise, returns false.
        """
        return date >= self.start_date and date <= self.end_date
    
    def overlaps(self, other):
        """
        Checks whether this date range overlaps for at least one day with
        another date range. Returns true if this date range overlaps with the
        other date range.
        """
        return (self.includes(other.start_date) 
                or self.includes(other.end_date))
        
    def overlap(self, other):
        """
        Determines the number of days in the overlap period between this date
        range and the other date range.
        """
        if not self.overlaps(other):
            return 0
        else:
            overlap_start_date = self.overlap_start_date(other)
            overlap_end_date = self.overlap_end_date(other)
            return ((overlap_end_date - overlap_start_date) + 
                    timedelta(days=1)).days
    
    def overlap_start_date(self, other):
        """
        Determines the start date of the overlap period between this date range
        and another date range.
        
        Assumes that this date range overlaps with the other date range.
        """
        if self.includes(other.start_date):
            return other.start_date
        else:
            return self.start_date
    
    def overlap_end_date(self, other):
        """
        Determines the end date of the overlap period between this date range
        and another date range.
        
        Assumes that this date range overlaps with the other date range.
        """
        if self.includes(other.end_date):
            return other.end_date
        else:
            return self.end_date