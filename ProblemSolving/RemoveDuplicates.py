# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates IN-PLACE such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(arr):
    numbersExists = set()

    for i in arr:
        if i not in numbersExists:
            numbersExists.add(i)
        else:
            continue
    
    return list(numbersExists)

# BETTER SOLUTION
def removeDuplicates(arr):
    #  arr =  doesn't replace elements in the original list.
    #  arr[:] = replaces element in place
    arr[:] = sorted(set(arr))
    return arr

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))