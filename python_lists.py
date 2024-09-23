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


list = [1,2,3,4,5,6]
list2 = [5,7,12,6,3]

#O(n) because it is itterating over the list
print(square_list(list))

#O(n) where n is the number of items in the provided sublist 
print(reverse_sublist(list,2,5))

#O(n log n) where n ais the combined number of items in both lists, also the list is sorted at the end so thats where the log comes in becuase timsort is O(n log n) time
print(merge_lists(list,list2))