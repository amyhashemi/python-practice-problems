# B = [1,2,3,4,5,6,7]
# A = [4,5,6,7,1,2,3]

B = [1,2,3,4,5,6,7,3,5,2,1,5]
A = [4,5,6,7,1,2,3,9,10,11,12]

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]

list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3] #######
# is_rotation(list1, list2c) should return False. - this
list2d = [4, 6, 5, 7, 1, 2, 3] #######
# is_rotation(list1, list2d) should return False. - this
list2e = [4, 5, 6, 7, 0, 2, 3] #######
# is_rotation(list1, list2e) should return False. - this
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

def is_rotation(A, B):
    '''
    Determines if arrays A and B are rotations of one another (rearranged, but maintaining order)
    '''

    key = A[0]
    key_i = -1

    if len(A) != len(B):
        return False #we know right away that they are not the same length

    for i, item in enumerate(B):
        if item == key:
            key_i = i
            break
    
    #if it never found a match:
    if key_i == -1:
        return False
    
    for i, item in enumerate(A):
        j = (key_i + i) % len(A)
        if A[i] != B[j]:
            return False
        
    return True
    

#result = is_rotation(A, B)
result2a = is_rotation(list1, list2a)
result2b = is_rotation(list1, list2b)
result2c = is_rotation(list1, list2c)
result2d = is_rotation(list1, list2d)
result2e = is_rotation(list1, list2e)
result2f = is_rotation(list1, list2f)
result2g = is_rotation(list1, list2g)

print(result2a)
print(result2b)
print(result2c)
print(result2d)
print(result2e)
print(result2f)
print(result2g)