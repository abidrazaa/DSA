
# Sum of first n numbers

n = int(input('enter number: '))

# def addNumbers(i,ans):
#     if i>n:
#         print(ans)
#         return
#     addNumbers(i+1,ans+i)

# addNumbers(1,0)

# def addNumbers(i,ans):
#     if i<1:
#         print(ans)
#         return
#     addNumbers(i-1,ans+i)

# addNumbers(n,0)


# def addNumbers(i):

#     if i==n:
#         return i
#     return i + addNumbers(i+1)

# print(addNumbers(1))

def addNumbers(i):
    if i==1:
        return 1
    
    return i+addNumbers(i-1)

print(addNumbers(n))