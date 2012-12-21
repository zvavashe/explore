"""
An exploration of classical algorithms.
"""

def bubble_sort(l):
    """
    Bubble sort is known to be inefficient when sorting a large of data. The
    algorithm does not scale well - It has worst case and average complexity of
    O(n^2).
    
    The way it works:
    (1) Go through the elements of the list swapping elements for each case 
    where an element is less than its predecessor.
    (2) Repeat the above process until you can go through the whole list 
    without swapping any elements.
    """
    if len(l) in (0, 1):
        return l[:]
    
    l = l[:]
    swapped = True
    while swapped:  
        swapped = False      
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                swap(l, i-1, i)
                swapped = True

    return l

    
def swap(l, previous_position, current_position):
    """
    Swaps two items in a list.
    """
    l[previous_position], l[current_position] = l[current_position], l[previous_position]
    