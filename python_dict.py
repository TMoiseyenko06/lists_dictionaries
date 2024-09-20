#Task 1
def merge_dict(dict1,dict2):
    dict2.update(dict1)
    print(dict2)
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



