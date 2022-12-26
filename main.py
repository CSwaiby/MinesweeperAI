from board import Board
from scan import scan_board
import pyautogui
import algorithm

website = 'https://minesweeper.one/'
board = Board()

def long_pause():
    pyautogui.PAUSE = 3


def pause():

    pyautogui.PAUSE = 1


def new_game_in_new_window():
    pyautogui.FAILSAFE = True

    pyautogui.press('win')
    pause()
    pyautogui.write('chrome')  # USES CHROME AS BROWSER
    pause()
    pyautogui.click(pyautogui.locateOnScreen('chrome.png', confidence=0.9))
    pause()
    pyautogui.getWindowsWithTitle('Google Chrome')[0].maximize()
    pause()
    pyautogui.write(website)
    pyautogui.press('enter')
    long_pause()
    # Board()
    # print(Board.__str__(Board))


def start():
    pyautogui.click(pyautogui.locateOnScreen('button.png', confidence=0.9))
    pause()


new_game_in_new_window()
start()
board = scan_board()
print(board)
algorithm.go_for_rule1(board)
print(board)
pyautogui.moveTo(100, 400)
