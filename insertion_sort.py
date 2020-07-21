import random
A=[random.randint(0,20) for i in range(15)]

def insertion_sort(arr):
    swap_count=0
    iteration_count=0
    comparison_count=0
    for marker in range(1,len(arr)):
        traverser=marker
        print(f"Iteration {iteration_count}: {arr}")
        iteration_count+=1
        while traverser>0:
            comparison_count+=1
            if arr[traverser]<arr[traverser-1]:
                arr[traverser], arr[traverser-1] = arr[traverser-1], arr[traverser]
                swap_count+=1
                traverser-=1
            else: #without the else block the program still works but the program won't be efficient
                break
    print(f"Iteration {iteration_count}: {arr}") #Without this last iteration won't be printed
    return arr, comparison_count, swap_count

final_ans=insertion_sort(A)
print(f"\nSorted List: {final_ans[0]}\nNumber of Comparisons:{final_ans[1]}\nTotal number of swaps:{final_ans[2]}")


