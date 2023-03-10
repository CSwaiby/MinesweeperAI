import pyautogui
from board import Board
import cv2


def check_unopened():
    unopened = []

    for pos in pyautogui.locateAllOnScreen('button.png', confidence=0.95):
        unopened.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return unopened


def check_flag():
    flag = []

    for pos in pyautogui.locateAllOnScreen('flag.png', confidence=0.9):
        flag.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return flag


def check_empty():
    empty = []

    for pos in pyautogui.locateAllOnScreen('zero.png', confidence=0.9):
        empty.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return empty


def check_one():
    one = []

    for pos in pyautogui.locateAllOnScreen('one.png', confidence=0.655):
        one.append([round((pos.top - 230)/32), int((pos.left - 555)/32)])

    return one


def check_two():
    two = []

    for pos in pyautogui.locateAllOnScreen('two.png', confidence=0.655):
        print(f"two: top:{pos.top} and left: {pos.left}")
        two.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return two


def check_three():
    three = []

    for pos in pyautogui.locateAllOnScreen('three.png', confidence=0.9):
        three.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return three


def check_four():
    four = []

    for pos in pyautogui.locateAllOnScreen('four.png', confidence=0.9):
        four.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return four


def check_five():
    five = []

    for pos in pyautogui.locateAllOnScreen('five.png', confidence=0.9):
        five.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return five


def check_six():
    six = []

    for pos in pyautogui.locateAllOnScreen('six.png', confidence=0.9):
        six.append([int((pos.top - 230)/32), int((pos.left - 555)/32)])

    return six


def scan_board():
    brd = Board()
    sqr_dict = {}

    flag = check_flag()
    for i in range(len(flag)):
        print(f"flag {flag[i]}")
        sqr_dict.update({tuple(flag[i]): 11})

    unopened = check_unopened()
    for i in range(len(unopened)):
        print(f"button {unopened[i]}")
        sqr_dict.update({tuple(unopened[i]): 9})

    empty = check_empty()
    for i in range(len(empty)):
        print(f"empty {empty[i]}")
        sqr_dict.update({tuple(empty[i]): 0})

    one = check_one()
    for i in range(len(one)):
        print(f"one {one[i]}")
        sqr_dict.update({tuple(one[i]): 1})

    two = check_two()
    for i in range(len(two)):
        print(f"two {two[i]}")
        sqr_dict.update({tuple(two[i]): 2})

    three = check_three()
    for i in range(len(three)):
        print(f"three {three[i]}")
        sqr_dict.update({tuple(three[i]): 3})

    four = check_four()
    for i in range(len(four)):
        print(f"four {four[i]}")
        sqr_dict.update({tuple(four[i]): 4})

    five = check_five()
    for i in range(len(five)):
        print(f"five {five[i]}")
        sqr_dict.update({tuple(five[i]): 5})

    six = check_six()
    for i in range(len(six)):
        print(f"six {six[i]}")
        sqr_dict.update({tuple(six[i]): 6})

    # print(sqr_dict)
    k = 0
    for i in range(8):
        for j in range(8):
            brd.arr[k].set_status(sqr_dict.get(tuple([i, j])))
            k += 1

    return brd
