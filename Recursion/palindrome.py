
s = 'madami'
arr = list(s)

def checkPalindrome(idx):
    if arr[idx] != arr[len(arr)-1-idx]:
        return False

    if len(arr)/2<idx:
        return True
    
    return checkPalindrome(idx+1)


print(checkPalindrome(0))


