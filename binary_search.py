'''Returns the index position of the element in question, or -1 if the
element can't be found. Time complexity of O(log n).
'''

def binary_search(arr, elem):
    start = 0
    end = len(arr) - 1
    mid = (start + end)//2
    while arr[mid] != elem and start <= end:
        if elem < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
        mid = (start + end) // 2
    if arr[mid] == elem:
        return mid
    else:
        return -1

test_array = [2,5,6,9,13,15,28,30]
print(binary_search(test_array, 13))
#expected outcome is 4
print(binary_search(test_array, 16))
#expected outcome is -1
