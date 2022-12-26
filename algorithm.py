# The algorithm will be split into 3 rules, the AI will go through each,
# if one rule does apply, then it will act upon it without having to go through the other rules

# RULE 1:
# If the number of buttons around a numbered square are equal to the status of the numbered square,
# then, flag all those buttons as mines (status = 11)

# RULE 2:
# If the number of mines around a numbered square are equal to the status of the numbered square,
# then, all other unopened buttons around it are safe and should be clicked (left click)

# RULE 3:
# Creating a matrix where the unknown numbers are the neighboring uncovered buttons of numbered squares,
# hence creating a matrix where the equations are the sum of these unknowns
# equal to each neighboring numbered square.
# Check https://massaioli.wordpress.com/2013/01/12/solving-minesweeper-with-matricies/

# If the AI passes through all 3 rules and still cannot find a 100% safe square to open,
# then it will calculate the probability of each square using the third rule's results
def get_surrounding(square, board):
    xcoord = square.xcoord
    ycoord = square.ycoord
    arr = [[xcoord - 1, ycoord - 1], [xcoord, ycoord - 1], [xcoord + 1, ycoord - 1],
           [xcoord - 1, ycoord], [xcoord + 1, ycoord],
           [xcoord - 1, ycoord + 1], [xcoord, ycoord + 1], [xcoord + 1, ycoord + 1]]
    tmp = [[xcoord - 1, ycoord - 1], [xcoord, ycoord - 1], [xcoord + 1, ycoord - 1],
           [xcoord - 1, ycoord], [xcoord + 1, ycoord],
           [xcoord - 1, ycoord + 1], [xcoord, ycoord + 1], [xcoord + 1, ycoord + 1]]
    # print(tmp[7][1])
    for i in tmp:
        if i[0] < 0 or i[0] > 7:
            arr.remove(i)
            continue
        if i[1] < 0 or i[1] > 7:
            arr.remove(i)
            continue

    main_arr = []
    for j in arr:
        main_arr.append(board.arr[(j[0]) + (j[1] * 8)])
    return main_arr


# Find neighbouring unopened squares:
def find_unopened(neighbouring_squares, board):
    unopened_neighbouring_squares = []
    for i in neighbouring_squares:
        if i.status == 9:
            unopened_neighbouring_squares.append(i)
    return unopened_neighbouring_squares


# Rule 1: (will only be called for numbered squares)
def rule1(square, board):
    unopened = find_unopened(get_surrounding(square, board), board)
    if len(unopened) == square.status:
        for i in unopened:
            i.flag()


# Find the numbered squares in board:
def find_numbered(board):
    numbered_squares = []
    for k in range(64):
        if 1 <= board.arr[k].status <= 6:
            numbered_squares.append(board.arr[k])

    return numbered_squares


def go_for_rule1(board):
    numbered_squares = find_numbered(board)
    for i in numbered_squares:
        rule1(i, board)
