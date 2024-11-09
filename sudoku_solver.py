board = [
    [7,8,0,4,0,0,1,2,0],   
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

'''
Description: Recursively solves the Sudoku board using backtracking.

Parameters:
bo (list of lists): 2D list representing the Sudoku board.

Return: Boolean values - True if solved; False if no solution.
'''

def solve(bo) -> bool:
    find = find_empty(bo) #find = (i, j) -> (row #, col #)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): 
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
'''
Description: Checks if num can be placed at pos without violating Sudoku rules.

Parameters:
bo: list representing the Sudoku board.
num: the number to validate
pos: (row, col) position to validate.

Returns: True if valid; False if invalid.
'''

def valid(bo, num, pos) -> bool: #example: num = 2 and pos = (3, 5) -> (row, column)
    # Check row
    for i in range(len(bo[0])): 
        if bo[pos[0]][i] == num:
            return False

    # Check column
    for i in range(len(bo)): 
        if bo[i][pos[1]] == num:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

'''
Description: Prints the Sudoku board in a formatted style.

Parameters:
bo: list representing the Sudoku board.

Returns: None
'''
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") #end"" is done to prevent a newline character because we continue printing the rows

'''
Description: Finds the first empty cell (0) on the board.

Parameters:
bo: list representing the Sudoku board.

Returns:
tuple or None: (row, col) of the first empty cell, or None if none exist.
'''

def find_empty(bo) -> tuple:
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("")
print("Solution: ")
print("")
print_board(board)