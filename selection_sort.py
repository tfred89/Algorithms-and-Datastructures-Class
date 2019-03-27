'''
Python example of selection sort, in which the smallest values
of an unordered array are iteratively moved to the left side of the array.
Iterating through a nested for loop results in O(n**2) time complexity
'''
def selection_sort(arr):
    for i in range(len(arr)):
        cur_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j
        if i != cur_min:
            arr[i], arr[cur_min] = arr[cur_min], arr[i]
    return arr

print(selection_sort([3,6,2,78,43,56,22,99,3,356]))
