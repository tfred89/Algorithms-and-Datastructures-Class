''' A simple function to search an array for a specific value, returning the
position of the array, or -1 if the value is not found. A single loop through
the array is required, resulting in a time complexity of O(n)
'''
def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

print(linear_search([34,51,1,2,3,45,56,687], 100))
print(linear_search([34,51,1,2,3,45,56,687], 51))
