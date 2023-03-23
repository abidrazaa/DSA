# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# EXAMPLE#1

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# EXAMPLE#2

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# EXAMPLE#3

# Input: nums = [3,3], target = 6
# Output: [0,1]


# BRUTE FORCE
def twoSum(arr, target):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
    return -1


# BETTER APPROACH
def twoSumIndexes(arr,target):
    d = {}
    for idx, num in enumerate(arr):
        r = target - num
        if r in d:
            return [idx,d[r]]
        d[num]=idx
    return -1


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSumIndexes([2,7,11,15], 9))
print(twoSumIndexes([3,2,4], 6))
print(twoSumIndexes([3,3], 6))



