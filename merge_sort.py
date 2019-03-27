'''
A function that sorts unordered arrays by recursively dividing
an array into subarrays of length 1 or 0, then combining them
with a function that sorts them. Results in a time complexity of
O(n log n)
'''
def merge(arr1, arr2): # a helper function to combine arrays in order
    result = []
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] < arr1[i]:
            result.append(arr2.pop(j))
        else:
            result.append(arr1.pop(i))
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

print(merge_sort([5,22,4,0, 67, 43, 15]))
