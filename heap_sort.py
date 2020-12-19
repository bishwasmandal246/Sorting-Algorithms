cnt = 0
def heapify(arr, n, i):
    global cnt
    largest = i
    left = (2*i) +1
    right = (2*i) +2

    if left<n:
        if right<n:
            cnt+=1
            print("Comparison",cnt,":",arr[left],",",arr[right])
            if arr[left]<arr[right]:
                cnt+=1
                print("Comparison",cnt,":",arr[right],",",arr[i])
                if(arr[right]>arr[i]):
                    arr[i],arr[right] = arr[right],arr[i]
                    heapify(arr,n,right)
            else:
                cnt+=1
                print("Comparison",cnt,":",arr[left],",",arr[i])
                if arr[left]>arr[i]:
                    arr[i],arr[left] = arr[left],arr[i]
                    heapify(arr, n,left)
        else:
            cnt+=1
            print("Comparison",cnt,":",arr[left],",",arr[i])
            if arr[left]>arr[i]:
                arr[i],arr[left] = arr[left], arr[i]
                heapify(arr,n,left)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [43,50,74,28,61,89,17,35]
heapsort(arr)
print("Total number of Comparisons=",cnt)
print("Sorted Array=", arr)
