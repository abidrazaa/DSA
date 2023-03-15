# Return an output array of the same length, where each element in the output array is equal to the product of
# every other number in the input array

def arrayOfProducts(arr):
    prod = 1
    res = []
    for i in arr:
        prod*=i
    
    for n in arr:
        res.append(prod//n)

    return res

print(arrayOfProducts([5, 1, 4, 2]))