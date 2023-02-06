

# Print names n times using recursion

# name = input('enter name: ')
# times = int(input('enter times: '))

# def printName(i):
#     if i>times:
#         return
#     print(name)
#     printName(i+1)

# printName(1)




# Print linearly 1 to n

# n = int(input('enter number: '))

# def printNumber(i):
#     if i>n:
#         return
#     print(i)

#     printNumber(i+1)

# printNumber(1)





# Print linearly 1 to n by BACKTRACKING (you can not use function(i+1))


# n = int(input('enter number: '))

# def printNumber(i):
#     if i<1:
#         return
    
#     printNumber(i-1)

#     print(i)

# printNumber(n)







# Print linearly n to 1 by BACKTRACKING (you can not use function(i-1))

n = int(input('enter number: '))

def printNumber(i):
    if i>n:
        return

    printNumber(i+1)
    print(i)


printNumber(1)
