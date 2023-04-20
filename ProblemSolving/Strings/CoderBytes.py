def StringChallenge(strParam):

    challengeToken = 'ikzy8muwb4e'

    res = ''
    prev = 0
    count = 1
    for i in range(1,len(strParam)):
        if strParam[i] == strParam[prev]:
            count+=1
            if i==len(strParam)-1:
                res += str(count)+strParam[prev]
        else:
            res += str(count)+strParam[prev]
            count=1
            if i==len(strParam)-1:
                res += '1'+strParam[i]
        prev+=1
    
    res+=challengeToken
    
    times = len(res)//4
    idx = 3
    res= list(res)
    for i in range(times):
        res[idx] = "_"
        idx+=4


    return ("".join(res))



print(StringChallenge('aabbcde'))
print(StringChallenge('wwwbbbw'))
