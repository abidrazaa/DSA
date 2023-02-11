arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

# Write a function that takes in two non-empty array of integers. Find the pair of numbers(one form each array) whose
# absolute difference closest to zero.
def smallestDifference(arr1,arr2):

    arr1.sort()
    # [-1,3,5,10,20,28]
    arr2.sort()
    # [15,17,26,134,135]

    pointerOne = 0
    pointerTwo = 0
    pair = (-1,-1)
    smallestDiff = float('inf')

    while pointerOne<len(arr1) and pointerTwo<len(arr2):
        firstNum = arr1[pointerOne]
        secondNum = arr2[pointerTwo]

        diff = abs(firstNum-secondNum)

        if firstNum > secondNum:
            pointerTwo+=1
        elif firstNum < secondNum:
            pointerOne+=1
        else:
            return (firstNum,secondNum)
        
        if diff < smallestDiff:
            smallestDiff = diff
            pair = (firstNum,secondNum)

    print(pair)

smallestDifference(arrayOne,arrayTwo)