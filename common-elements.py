A = [1,3,4,6,7,9,54,15]
B = [1,2,4,5,9,10,13,15,22,54]

def commonElements(A, B):
    '''
    Finds and returns a list of common elements between arrays A and B
    '''

    output = []
    p1 = 0
    p2 = 0

    while p1 < len(A) and p2 < len(B):
        if A[p1] == B[p2]:
            output.append(A[p1])
            p1+=1
            p2+=1

        elif A[p1] < B[p2]:
            p1+=1
        else:
            p2+=1

    return output

output = commonElements(A, B)
print(output)




