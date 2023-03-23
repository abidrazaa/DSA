# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# EXAMPLE#1:

# Input: s = "leetcode"
# Output: 0

# EXAMPLE#2:

# Input: s = "loveleetcode"
# Output: 2

# EXAMPLE#3:

# Input: s = "aabb"
# Output: -1


def firstUnique(s):
    d = {}
    for i in range(len(s)):
        char = s[i]
        if char in d:
            d[char][0] +=1
        else:
            d[char] = [1,i]

    for key,value in d.items():
        if value[0]==1:
            return value[1]
    return -1

print(firstUnique('leetcode'))
print(firstUnique('loveleetcode'))
print(firstUnique('aabb'))
    


