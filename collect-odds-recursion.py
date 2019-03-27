''' A recursion example that creates a new list of all odd numbers
from an array of numbers
'''
def collect_odds(arr):
    new_list = []
    if len(arr) == 0:
        return new_list

    if arr[0] % 2 != 0:
        new_list.append(arr[0])

    new_list = new_list + collect_odds(arr[1:])
    return new_list

print(collect_odds([1,2,3,4,5,6,7,11,22,33,44,55,66,77]))
