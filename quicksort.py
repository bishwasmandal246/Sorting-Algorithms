import random
A=[random.randint(0,20) for i in range(15)]

def quicksort(arr): #Naive Approach as the space required is way too much. Use Inplace algorithm for efficiency
    if len(arr)<2:
        return arr
    else:
        small,middle,large=[],[],[]
        pivot=arr[-1]
        for num in arr:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                large.append(num)
        return quicksort(small)+middle+quicksort(large)

def desc_quicksort(arr): #Notice that this is not an inplace function
    if len(arr)<2:
        return arr
    else:
        small,middle,large=[],[],[]
        pivot=arr[-1]
        for num in arr:
            if num > pivot:
                small.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                large.append(num)
        return desc_quicksort(small)+middle+desc_quicksort(large)
print(desc_quicksort(A))

def quicksort_inplace(arr):
    if len(arr)<2:
        return arr
    else:
        i=-1
        j=0
        pivot=arr[-1]
        while j < len(arr)-1:
            if pivot>arr[j]:
                swap=True
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
        i+=1
        arr[i],arr[-1]=arr[-1],arr[i]
        return quicksort(arr[:i])+[arr[i]]+quicksort(arr[i+1:])

def desc_quicksort_inplace(arr):
    if len(arr)<2:
        return arr
    else:
        i=-1
        j=0
        pivot=arr[-1]
        while j < len(arr)-1:
            if pivot<arr[j]:
                swap=True
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
        i+=1
        arr[i],arr[-1]=arr[-1],arr[i]
        return quicksort(arr[:i])+[arr[i]]+quicksort(arr[i+1:])

print("your result as per your convinience")
