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

def get_surrounding(xcoord, ycoord):
    arr = [[xcoord - 1, ycoord - 1], [xcoord, ycoord - 1], [xcoord + 1, ycoord - 1],\
        [xcoord - 1, ycoord], [xcoord + 1, ycoord],
        [xcoord - 1, ycoord + 1], [xcoord, ycoord + 1], [xcoord + 1, ycoord + 1]]
    tmp = [[xcoord - 1, ycoord - 1], [xcoord, ycoord - 1], [xcoord + 1, ycoord - 1],\
        [xcoord - 1, ycoord], [xcoord + 1, ycoord],
        [xcoord - 1, ycoord + 1], [xcoord, ycoord + 1], [xcoord + 1, ycoord + 1]]
    # print(tmp[7][1])
    k = 0
    print(tmp)
    for i in tmp:
        if i[0] < 0 or i[0] > 7:
            arr.remove(i)
            continue
        if i[1] < 0 or i[1] > 7:
            arr.remove(i)
            continue
        k += 1

    return arr

    # print(tmp)
    # print(tmp[i])
    # print(k)
    # print(i)
    # if tmp[i][0] < 0 or tmp[i][0] > 7:
    #     tmp.pop(k)
    #     print("first")
    #     i -= 1
    #     continue
    # if tmp[i][1] < 0 or tmp[i][1] > 7:
    #     tmp.pop(k)
    #     print("second")
    #     i -= 1
    #     continue
    # k += 1


    # if xcoord != 0 or 7:
    #     if ycoord != 0 or 7:
    #         return [(xcoord - 1, ycoord - 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord - 1),
    #                 (xcoord - 1, ycoord), (xcoord + 1, ycoord),
    #                 (xcoord - 1, ycoord + 1), (xcoord, ycoord + 1), (xcoord + 1, ycoord + 1)]
    #     elif ycoord % 8 == 0:
    #         return [(xcoord - 1, ycoord), (xcoord + 1, ycoord),
    #                 (xcoord - 1, ycoord + 1), (xcoord, ycoord + 1), (xcoord + 1, ycoord + 1)]
    #     else:
    #         return [(xcoord - 1, ycoord - 1), (xcoord, ycoord - 1), (xcoord + 1, ycoord - 1),
    #                 (xcoord - 1, ycoord), (xcoord + 1, ycoord)]
    # elif xcoord == 0:
    #     if ycoord != 0 or 7:
    #         return [(xcoord, ycoord - 1), (xcoord + 1, ycoord - 1),
    #                 (xcoord + 1, ycoord),
    #                 (xcoord, ycoord + 1), (xcoord + 1, ycoord + 1)]
    #     elif ycoord == 0:
    #         return [(xcoord + 1, ycoord),
    #                 (xcoord, ycoord + 1), (xcoord + 1, ycoord + 1)]
    #     else:
    #         return [(xcoord, ycoord - 1), (xcoord + 1, ycoord - 1),
    #                 (xcoord + 1, ycoord)]
    # else:
    #     if ycoord != 0 or 7:
    #         return [(xcoord - 1, ycoord - 1), (xcoord, ycoord - 1),
    #                 (xcoord - 1, ycoord),
    #                 (xcoord - 1, ycoord + 1), (xcoord, ycoord + 1)]
    #     elif ycoord == 0:
    #         return [(xcoord - 1, ycoord),
    #                 (xcoord - 1, ycoord + 1), (xcoord, ycoord + 1)]
    #     else:
    #         return [(xcoord - 1, ycoord - 1), (xcoord, ycoord - 1)
    #                 (xcoord - 1, ycoord)]
