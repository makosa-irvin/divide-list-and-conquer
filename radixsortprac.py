

def rs(ul_list):
    #finding maximum number
    max_number = max(ul_list)
    max_value = len(str(max_number))
    #making a copy
    ulist = ul_list[:]
    
    #iterate through all place values
    for val in range(max_value):
        #position and index on right side(starting with ones)
        position = val + 1
        index = -position
        
        #creating ten buckets to store the diff values from  0 to 9
        buckets = [[]for bucket in range(10)]
        #iterate through each number in list
        for number in ulist:
            #converting number to string
            num_string = str(number)
            #fetching the said digit
            try:
                digit = num_string[index]
            except IndexError:
                digit = 0
            digit= int(digit)    
            buckets[digit].append(number)
            
        ulist = []
        for num in buckets:
            ulist.extend(num)
            
    return ulist

#calling rs
unsorted_list = [344,21,534235,45,23,4235,45423,7898,87,56,6]
sorted_list = rs(unsorted_list)
print(sorted_list)
            
            
                
    