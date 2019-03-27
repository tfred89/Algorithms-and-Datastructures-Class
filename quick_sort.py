''' A sorting function that determines a pivot point, the recursively
places values lower than the pivot to the left and higher to the right.
This results in a time complexity of O(n log n).

Note that this solution could be optimized by implementing a 'pivot' function,
which would not require new arrays to be built.
'''
def quick_sort(arr):
    less = []
    equal = []
    greater = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)

        return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([45,32,11,5,98,30,18]))
