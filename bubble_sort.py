''' Sorts an unordered array by moving the largest values to the end of the
array, so they "bubble" to the top, resulting in a time complexity of O(n**2) (avg)
'''
def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        no_swap = True
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                no_swap = False
        if no_swap:
            break
    return arr

print(bubble_sort([4,22,5,67,11,90]))
