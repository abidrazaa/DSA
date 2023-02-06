

n = int(input('enter number: '))

# def factorial(i):
#     if i==1:
#         return 1
    
#     return i*factorial(i-1)

# print(factorial(n))

def factorial(i,product):
    if i<1:
        print(product)
        return
    factorial(i-1,product*i)

factorial(n,1)