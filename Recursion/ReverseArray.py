
# Reverse an array by recursion

arr = [1,2,3,4,5]

def reverseArray(firstPointer,secondPointer):
    if firstPointer>=secondPointer:
        print(arr)
        return

    arr[firstPointer],arr[secondPointer] = arr[secondPointer],arr[firstPointer]

    reverseArray(firstPointer+1,secondPointer-1)

reverseArray(0,len(arr)-1)



def reverseArray(pointer):
    if (len(arr)/2)<=pointer:
        print(arr)
        return
    
    arr[pointer],arr[len(arr)-1-pointer] = arr[len(arr)-1-pointer],arr[pointer]
    reverseArray(pointer+1)

reverseArray(0)