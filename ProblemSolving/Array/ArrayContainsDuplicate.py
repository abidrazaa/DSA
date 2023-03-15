# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# EXAMPLE#1

# Input: nums = [1,2,3,1]
# Output: true

# EXAMPLE#2

# Input: nums = [1,2,3,4]
# Output: false


def containsDuplicates(nums):
    numbers = set()

    for i in nums:
        if i in numbers:
            return True
        else:
            numbers.add(i)
    return False


print(containsDuplicates([1,2,3,1]))
print(containsDuplicates([1,2,3,4]))
