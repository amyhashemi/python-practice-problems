import queue

def mine_sweeper(bombs, num_rows, num_cols):
    '''
    Creates a 2D array, while assigning bomb and number locations for a minesweeper game. 
    Iterates through the array systematically and keeps track of iterators and the size of the 
    array so that we don't try to assign a cell that doesn't exist a value.
    '''

    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    #assign bomb locations

    for bomb in bombs: 
        row_i = bomb[0]
        col_i = bomb[1]  
        field[row_i][col_i] = -1
        for i in range(row_i-1, row_i+2):
            for j in range(col_i-1, col_i+2):
                if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j]+=1


    return field

def click(field, num_rows, num_cols, given_i, given_j):
    '''
    Params: field: a 2D array depicting a minesweeper field
            num_rows: number of rows in the field
            num_cols: number of columns in the field
            given_i: row position where the user wants to click
            given_j: column position where the user wants to click

            Soluton uses Breadth-First search to scan all surrounding cells for 0's
    '''
    #to_check queue for storing the next coordinates to check - pop off the top as we check them
    to_check = queue.Queue()
    current_i = given_i
    current_j = given_j

    if (field[current_i][current_j] != 0):
        return field
    else:
        #store cell coordinates in to_check if it is a zero and then change the value to -2 -- we want to check the cells surrounding that cell later
        field[current_i][current_j] = -2
        to_check.put((current_i, current_j))

        while not to_check.empty():
            (current_i, current_j) = to_check.get()
            for i in range(current_i-1, current_i+2):
                for j in range(current_j-1, current_j+2):
                     if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] == 0): #only if the current coordnates are actually positions in the array do we check
                        to_check.put((i, j))
                        field[i][j] = -2

    return field





# using output from the last function
# field = mine_sweeper(([1,0],[0,1]), 3, 4)

# field = click(field, 3, 4, 0, 3)

# print(field[0])
# print(field[1])
# print(field[2])

#test cases

field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

field = click(field1, 3, 5, 2, 2)

print(field[0])
print(field[1])
print(field[2])
print("_________")

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]

field = click(field1, 3, 5, 1, 4)

print(field[0])
print(field[1])
print(field[2])
print("_________")

# Next test case

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

field = click(field2, 4, 4, 0, 1)

print(field[0])
print(field[1])
print(field[2])
print("_________")

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]

field = click(field2, 4, 4, 1, 3)

print(field[0])
print(field[1])
print(field[2])
print("_________")



