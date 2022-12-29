from board import Board
from scan import scan_board
from actions import *
import algorithm

board = Board()
new_board = Board()

new_game_in_new_window()
start()
board = scan_board()
print(board)
# while new_board != board:
#     new_board = board
#     print(new_board)
#     algorithm.go_for_rule1(board)
#     # print(board)
#     algorithm.go_for_rule2(board)
#     board = scan_board()
#     print(board)

pyautogui.moveTo(100, 400)
