
from random import randrange
def qs(list,start,end):
    if start>=end:
        return
    p_idx = randrange(start,end+1)
    p_elem = list[p_idx]
    #print("the former list {0} with pivot {1}".format(list,p_elem))
    
    list[p_idx],list[end]=list[end],list[p_idx]
    #print("the later list {0} with pivot {1}".format(list,p_elem))
    less_than_point = start
    for i in range(start,end):
        if list[i]<p_elem:
            list[less_than_point],list[i] = list[i],list[less_than_point]
            less_than_point += 1
    
    
        
    list[end],list[less_than_point]=list[less_than_point],list[end]
    
    
    qs(list,start,less_than_point-1)
    
    qs(list,less_than_point+1,end)
    return list

un_list = [21,54,655,754,234,22,554,231]
lst = qs(un_list,0,len(un_list)-1)
print (lst)
    