''' Sorts an unordered array by gradually building a sorted left-side of the
array. Potential nested iteratively loop results in O(n**2) time complexity
'''

def insertion_sort(arr):
    for i in range(len(arr)):
        current = arr[i]
        position = i
        while position > 0 and current < arr[position - 1]:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current

    return arr

print(insertion_sort([4,1,7,34,22,89,5]))
