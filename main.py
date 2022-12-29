from board import Board
from scan import scan_board
from actions import *
import algorithm

board = Board()


new_game_in_new_window()
start()
board = scan_board()
print(board)
algorithm.go_for_rule1(board)
print(board)
pyautogui.moveTo(100, 400)
