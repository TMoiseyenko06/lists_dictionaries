#Task 1
def merge_dict(dict1,dict2):
    dict2.update(dict1)
    return dict2

#Task 2
def intersect_dict(dict1,dict2):
    intersection = {k:dict1[k] for k in dict1 if k in dict2}
    return intersection

#Task 3
def frequency(arr):
    result = {}
    for item in arr:
        if item in result:
           result[item] += 1; 
        else:
            result[item] = 1;
    return result


dict1 = {1:1,2:2}
dict2 = {1:1,3:3}
array = [1,1,2,4,6,5,3,2,45,6,7,5]

#Time complexitty is O(n) where n is the number of items in the first dictionary
print(merge_dict(dict1,dict2))

#Time complexity is also O(n) where n is the number of item in dict1
print(intersect_dict(dict1,dict2))

#Also O(n) time becuase it has to itterate through the given array, and the time complexity of adding the items to the dictionary is O(1) because of the unique keys
print(frequency(array))