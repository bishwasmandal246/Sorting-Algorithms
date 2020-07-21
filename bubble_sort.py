import random
A=[random.randint(0,20) for i in range(15)]

def bubble_sort(arr):
    swap_happened=True
    comparison_count=0
    iteration_count=0
    swap_count=0
    while swap_happened:
        swap_happened=False
        print(f"Iteration {iteration_count}: {arr}")
        iteration_count += 1
        for i in range(len(arr)-1):
            comparison_count+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap_happened=True
                swap_count+=1
    return arr, comparison_count, swap_count

final_ans = bubble_sort(A)
print("Final Sorted List is",final_ans[0],"\nNumber of Comparisons:",final_ans[1],"\nTotal Number of swaps:",final_ans[2])
