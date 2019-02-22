# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:54:42 2019

@author: User
"""

def merge_sort(my_list):
    
    if len(my_list)<=1:
       return my_list
    mid_idx = len(my_list)//2
    left_sublist = my_list[:mid_idx]
    right_sublist = my_list[mid_idx:]
    
    left_sort = merge_sort(left_sublist)
    right_sort = merge_sort(right_sublist)
    
    return compare(left_sort,right_sort)
   
   
   
def compare(left,right):
    
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            
    if left:
        result+=left
        
    if right:
        result+=right
        
    return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
ordered_list1 = merge_sort(unordered_list1)
ordered_list2 =merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)
print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
        
   