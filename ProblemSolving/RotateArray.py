# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#EXAMPLE#1

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


def rotateArray(array,jumps):
    newArr = [0 for i in array]

    for curr in range(len(array)):
        newPosition = (curr+jumps)%len(array)
        newArr[newPosition] = array[curr]

    return newArr

print(rotateArray([1,2,3,4,5,6,7],3))