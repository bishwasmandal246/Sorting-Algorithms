import random
A=[random.randint(0,15) for i in range(15)]

def merge(arr1,arr2):
    i,j=0,0
    merged_sorted=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_sorted.append(arr1[i])
            i+=1
        else:
            merged_sorted.append(arr2[j])
            j+=1
    if i<len(arr1):
        merged_sorted.extend(arr1[i:])
    if j<len(arr2):
        merged_sorted.extend(arr2[j:])
    return merged_sorted

def divide_merge(arr1):
    if len(arr1)<2:
        return arr1
    else:
        divider=len(arr1)//2
        divided_list1= divide_merge(arr1[:divider])
        divided_list2= divide_merge(arr1[divider:])
        return merge(divided_list1,divided_list2)

print(divide_merge(A))