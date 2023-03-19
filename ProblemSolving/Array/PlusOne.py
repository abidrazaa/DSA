# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# EXAMPLE#1

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# EXAMPLE#2

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# EXAMPLE#3

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].



# BRUTE FORCE APPROACH
def plusOneToArray(digits):
    s=''
    for i in digits:
        s+=str(i)
    a = int(s)
    a+=1
    s = list(str(a))
    out = []
    for i in s:
        out.append(int(i))
    return out



# BETTER SOLUTION
def plusOne(arr):
    # joining elements of an array after converting each element(integer) into a string
    # because .join() takes an array of strings as the argument
    number = int("".join(map(str,arr)))

    number = str(number+1)

    output = [int(i) for i in number]

    return output

    


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
