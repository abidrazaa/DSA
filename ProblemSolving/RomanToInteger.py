def romanToInteger(s):
    
    lookup = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }

    number = 0

    for i in range(len(s)):
        if (i+1)!=len(s) and lookup[s[i]]<lookup[s[i+1]]:
            number-=lookup[s[i]]
        else:
            number+=lookup[s[i]]
        
    return number


s = 'XIV'

print(romanToInteger(s))


