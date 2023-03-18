# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# EXAMPLE#1

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# EXAMPLE#1

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# BRUTE FORCE
def intersect(arr1,arr2):

    count = {}
    res = []
    for i in arr1:
        if i in count:
            count[i][0]+=1
        else:
            count[i] = [1,0]
    for i in arr2:
        if i in count:
            count[i][1]+=1
        else:
            count[i] = [0,1]

    for x,y in count.items():
        times = min(y)
        while times>0:
            res.append(x)
            times-=1
    return res


# BEST
# Two pointers approach
def intersection(arr1,arr2):
    arr1.sort()
    arr2.sort()

    i=0
    j=0

    output = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            output.append(arr1[i])
            i+=1
            j+=1
    return output
        


print(intersection([4,9,5],[9,4,9,8,4]))
print(intersection([1,2,2,1],[2,2]))