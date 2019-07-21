def is_one_away(string1, string2):
    '''
    Returns True if either string1 or string2 are within one 
    edit away of being identical to one another. Operations include:
    Change: Changing a single character
    Delete: Deleting a single character
    Add: Adding a single character
    '''

    p1 = 0
    p2 = 0

    editcount = 0

    if abs(len(string1) - len(string2)) > 1:
        return False
    
    if len(string1) == len(string2):
        while p1 < len(string1) and p2 < len(string2):
            if string1[p1] != string2[p2]:
                editcount+=1
            p1+=1
            p2+=1
        if editcount > 1:
            return False
    
    if abs(len(string1) - len(string2)) == 1:
        while p1 < len(string1) and p2 < len(string2):
            if string1[p1] != string2[p2]:
                if len(string1) > len(string2):
                    p1+=1
                if len(string1) < len(string2):
                    p2+=1
                if string1[p1] != string2[p2]:
                    return False
            p1+=1
            p2+=1
    
    return True

ans = is_one_away("abcde", "abcd")  # should return True
print(ans)
ans = is_one_away("abde", "abcde")  # should return True
print(ans)
ans = is_one_away("a", "a")  # should return True
print(ans)
ans = is_one_away("abcdef", "abqdef")  # should return True
print(ans)
ans = is_one_away("abcdef", "abccef")  # should return True
print(ans)
ans = is_one_away("abcdef", "abcde")  # should return True
print(ans)
ans = is_one_away("aaa", "abc")  # should return False
print(ans)
ans = is_one_away("abcde", "abc")  # should return False
print(ans)
ans = is_one_away("abc", "abcde")  # should return False
print(ans)
ans = is_one_away("abc", "bcc")  # should return False
print(ans)