def merge(list1,list2):
    combined=[]
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i<len(list1):
        combined.append(list1[i])
        i+=1
        
    while j<len(list2):
        combined.append(list2[j])
        j+=1
    return combined

def mergesort(my_list):
    if len(my_list)==1:
        return my_list
    mid_value=int(len(my_list)/2)
    left=mergesort(my_list[:mid_value])
    right=mergesort(my_list[mid_value:])
    
    return merge(left,right)

my_list=[3,1,2,4]
print(mergesort(my_list))
print("original list:",my_list)