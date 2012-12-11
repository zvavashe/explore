"""
I wrote this code simply to explore the standard itertools module's 
functionality. 

It may appear that this code is over commented but that is not the case. Most
the 'comments' are just notes to myself. 
"""

from itertools import groupby

#the following was lifted from stackoverflow: 
#http://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby

things = [('animal', 'bear'), ('animal', 'duck'), ('plant', 'catcus'), 
          ('vehicle', 'speed boat'), ('vehicle', 'school bus')]

for key, group in groupby(things, lambda x: x[0]):
    print list(group)

#The above example is not very good though because the things list is already 
#sorted and one may end up wrongly assuming that function works  expected even 
#when passed an unsorted list of things. Thus the next #example to show how the 
#groupby function when starting off with an list that has not yet been sorted.
unsorted_things = [('vehicle', 'school bus'), ('animal', 'duck'), 
                   ('vehicle', 'speed boat'), ('animal', 'bear'), 
                   ('plant', 'catcus')]

#sort elements by thing type before applying the groupby function
sorted_things = sorted(unsorted_things, key = lambda x : x[0])

#confirm that the groupby functions returns the groups in the right order.
seen_groups = []
for key, group in groupby(sorted_things, lambda x : x[0]):
    if key not in seen_groups:
        seen_groups.append(key)
        
    if key == 'animal':
        assert 'plant' not in seen_groups
        assert 'vehicle' not in seen_groups
        
    if key == 'plant':
        assert 'animal' in seen_groups
        assert 'vehicle' not in seen_groups
    
    if key == 'vehicle':
        assert 'animal' in seen_groups
        assert 'plant' in seen_groups   
    
    