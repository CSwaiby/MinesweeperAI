import pyautogui

website = 'https://minesweeper.one/'


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


def start():
    pyautogui.click(pyautogui.locateOnScreen('button.png', confidence=0.9))
    pause()


def back_to_pixels(x, y):
    # new_coords = [int((pos.top - 230) / 32), int((pos.left - 555) / 32)]
    coordinates = [0, 0]
    coordinates[0] = int((x * 32) + 555)
    coordinates[1] = int((y * 32) + 230)
    return coordinates


def flag_click(square):
    coords = back_to_pixels(square.xcoord, square.ycoord)
    pyautogui.rightClick(coords[0], coords[1])


# doubleClick() and not click() since minesweeper.one does allow the double-clicking of numbered squares
# which will make solving the board much quicker
def left_click(square):
    coords = back_to_pixels(square.xcoord, square.ycoord)
    pyautogui.doubleClick(coords[0], coords[1])
