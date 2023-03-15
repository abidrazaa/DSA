# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# EXAMPLE # 1

# Input: nums = [2,2,1]
# Output: 1

# EXAMPLE # 2

# Input: nums = [4,1,2,1,2]
# Output: 4


# Best solution
def singleNumberCheck(nums):
    # we consider that every element exists two times so we make set of nums and multiply it by 2
    doubles = 2*sum(set(nums))

    # actual sum of the numbers in array nums is: 
    actualSumofNums = sum(nums)

    # if we want to figure out a number that exists only one time so:
    return (doubles-actualSumofNums)


def anotherSolution(nums):

    countMaintain = {}
    for i in nums:
        if i in countMaintain:
            countMaintain[i]+=1
        else:
            countMaintain[i]=1
    
    for key,value in countMaintain.items():
        if value==1:
            return key
    




print(singleNumberCheck([2,2,1]))
print(singleNumberCheck([4,1,2,1,2]))
print(anotherSolution([4,1,2,1,2]))
print(anotherSolution([2,2,1]))
