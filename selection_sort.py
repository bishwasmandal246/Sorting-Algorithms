import random
A=[random.randint(0,20) for i in range(15)]

def selection_sort(arr):
    iteration_count=0
    comparison_count=0
    swap_count=0
    for marker in range(len(arr)):
        print(f"Iteration {iteration_count}: {arr}")
        iteration_count += 1
        for traverser in range(marker,len(arr)):
            comparison_count+=1
            if arr[marker]>arr[traverser]:
                arr[marker],arr[traverser]=arr[traverser],arr[marker]
                swap_count+=1
    return arr,comparison_count,swap_count

final_ans=selection_sort(A)
print(f"\nSorted List: {final_ans[0]}\nNumber of Comparisons:{final_ans[1]}\nTotal number of swaps:{final_ans[2]}")
