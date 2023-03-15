def NumberRepetition(arr,target):
    
    leftMostIdx = binarySearch(arr,target,True)
    rightMostIdx = binarySearch(arr,target) 

    return rightMostIdx-leftMostIdx+1

def binarySearch(arr,target,leftMost=False):
    left = 0
    right = len(arr)-1
    idx = -1
    while right>=left:
        mid = (left+right)//2

        if arr[mid]==target:
            idx = mid
            # if want to get leftmost index of target number
            if leftMost:
                right = mid - 1
            else:
                left = mid + 1

        elif arr[mid]>target:
            right = mid - 1

        else:
            left = mid + 1
        
    return idx
    

arr = [1,1,1,1,2,2,3,3,3,3,3,4,5,6,7,8,9,9,9,9,9]
num = 1
print(NumberRepetition(arr,num))
