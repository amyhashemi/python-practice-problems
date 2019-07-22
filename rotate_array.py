import copy

def rotate_sub(i, j, n):
    new_i = j
    new_j = n - 1 - i

    return new_i, new_j

def rotate_array(given_array, n):

    new_array = copy.deepcopy(given_array)

    for i in range(n):
        for j in range(n):
            (new_i, new_j) = rotate_sub(i, j, n)
            new_array[new_i][new_j] = given_array[i][j]

    return new_array

a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

new_array = rotate_array(a1, 3)
print(new_array[0])
print(new_array[1])
print(new_array[2])

