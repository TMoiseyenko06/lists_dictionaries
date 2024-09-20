#Task 1
def square_list(arr):
    return [x**2 for x in arr]

#Task 2
def reverse_sublist(arr,i,j):
    arr[i:j] = reversed(arr[i:j])
    return arr

#Task 3
def merge_lists(arr1,arr2):
    arr = arr1 + arr2
    return sorted(arr)

