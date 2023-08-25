# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


# EXAMPLE#1

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# EXAMPLE#2

# Input: nums = [0]
# Output: [0]


# BRUTE FORCE APPROACH
def moveZeroes(arr):
    for i in range(len(arr)):
        if arr[i]!=0 and i>0:
            curr = i
            prev = i-1

            while arr[prev]==0 and prev>=0:
                arr[curr],arr[prev] = arr[prev],arr[curr]
                curr = prev
                prev-=1
    return arr

# BETTER SOLUTION
def moveZeroesToEnd(arr):
    
    for i in range(len(arr)):
        if arr[i]==0:
            arr.pop(i)
            arr.append(0)
    return arr


print(moveZeroesToEnd([0,1,0,3,12]))
print(moveZeroesToEnd([0]))


            
# def move_zeros(arr):
# 	Length_of_array = len(arr)
# 	Idx = 0
# count=0
# for i in in range(len(arr)):
# 	If arr[i]!=0:
# 		arr[idx]=arr[i]
# 		idx+=1
# 		Else:
# 			count+=1
	
# 	While idx < len(array):
# 		Arr[idx] = 0 //O(M)

# O(N+M)

