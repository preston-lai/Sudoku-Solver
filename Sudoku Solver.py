#Sudoku Rules:
#Can't have the same number in the same box, column, or row

#Solution 1: Brute Force
#1 Pick empty square
#2 Try all numbers in the board (1, 2, 3, ...)
#3 Find one that works
#4 Repeat from beginning

#Solution 2: Backtracking Algorithm
#where solution cannot be completed, continue from previous step and restart
#if it's still not valid, keep going back

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

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    #basic case recursion - process of defining a problem/solution in
    #simplier terms

    for i in range(1,10):
        #loop through values from 1 to 9 (10 not included)
        if valid(bo, i, (row, col)):
            #if adding through values to a board, will it be a valid solution?
            bo[row][col] = i
            #if yes run this

            if solve(bo):
                #then call again with value added to keep trying to find a solution
                #or if we can't a solution after trying all values - return False
                #if we find a solution - return True
                return True

            bo[row][col] = 0


    return False

def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            #check each element in the row [i]
            #pos[1] = if its the number we just inputted, ignore
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box - which box we are in [0,1], [0,2], ...
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        #need to multiply 3 to get to each box
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                #check if any value in the box is equal to the one we just added
                #check that we aren't checking the same value we just added in
                    return False

    return True

def print_board(bo):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            #for every 3 rows print this line
            #% = remainder and ...
            print("------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                #if value is a multiple of 3 and not equal to 0
                print(" | ", end="")
                #drawing the lines of the Sudoku box

            if j == 8:
                #if value at last position
                print(bo[i][j])
                #go to the last line
            else:
                print(str(bo[i][j]) + " ", end="")
                #end="" means stay on the same line

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, col (y, x)

    return None
#if no blank squares - return None

print("Original Sudoku Board")
print_board(board)
solve(board)
print("")
print("")
print("")
print("Solved Sudoku Board")
print_board(board)








