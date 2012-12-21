import unittest

from explore_algorithms import bubble_sort

class TestBubbleSort(unittest.TestCase):
    """
    Unit tests for the bubble sort implementation.
    """
    
    def test_empty_list(self):
        """
        Test sorting with an empty list. Must return an empty list.
        """
        l = bubble_sort([])
        self.assertTrue(not l, "Must return back an empty list.")
        
    def test_single_element_list(self):
        """
        Test sorting with a list that has a single element. Must return list
        with single element.
        """
        a = [1]      
        l = bubble_sort(a)
        self.assertTrue(len(l) == 1, 
                        "Must return list with a single element.")
        self.assertTrue(l[0] == 1, 
                        "Must return the same element added to the list")
        
    def test_bubble_sort(self):
        """
        Test sorting with lists that have more than one element.
        """
        a = [3, 2, 1]
        l = bubble_sort(a)
        self.assertTrue(l[0] == 1, 
                        "One (1) must be first element of sorted list.")
        self.assertTrue(l[1] == 2, 
                        "Two (2) must be the second element of list.")
        self.assertTrue(l[2] == 3, 
                        "Three must be the last element of sorted list")
        
        