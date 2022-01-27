def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)
    
    #  keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range (9) is 0,1,2,3..8
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # if no space in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if it is valid, False if otherwise.

    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    # and now the square
    # in this next step, we want to know where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row _start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exist
    # mutates puzzle to be the solution ( if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

# step 1.1: if there's nowhere left, we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3,....9
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
