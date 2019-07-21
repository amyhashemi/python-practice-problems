
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
    '''

    



field = mine_sweeper(([1,0],[0,1]), 3, 4)

print(field[0])
print(field[1])
print(field[2])