# s = 'abcd'
# t = 'bcde'
s = 'abyz'
t = 'bcza'

character_map = {chr(i): i for i in range(ord('a'), ord('z')+1)}

def checkStrings(s,t):
    for i in range(len(s)):
        if character_map[s[i]] == character_map[t[i]]-1:
            continue
        elif s[i]=='z' and character_map[t[i]]==character_map['a']:
            continue
        else:
            return False

    return True

print(checkStrings(s,t))