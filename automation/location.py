"""
Choose board or game location
"""

import pyautogui as gui

import cv2 as cv
import numpy as np

import mss
import mss.tools

from typing import List


import win32gui
from screenshot import take_screenshot
def enumHandler(hwnd, lParam):
    window_name = win32gui.GetWindowText(hwnd).lower()
    if 'blackhole' in window_name or 'wormwhole' in window_name:
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        # ignore (1, 1)
        if (w > 100 or h > 100):
            global location
            location = [x, y, w, h]

def get_location_manually() -> List[int]:
    """
    Get the board location on the screen
    """
    input('Move to top left of the board and press enter')
    one = gui.position()
    input('Move to bottom right of the board and press enter')
    two = gui.position()

    print("Board Location - [{}, {}, {}, {}]".format(one.x, one.y, two.x, two.y))
    return [one.x, one.y, two.x, two.y]

def get_location_automatically():
    """
    Get the board location automatically on the screen
    """
    win32gui.EnumWindows(enumHandler, None)
    if (location != None):
        print('Found window at {}'.format(location))
        [x, y, w, h] = location
        # adjust it with manual offset because blackhole has additional controls
        top = y + 58
        left = x + 118
        width = w - 140
        height = h - 90
        
        game_img = np.array(take_screenshot({"top": top, "left": left, "width": width, "height": height}))
        gray = cv.cvtColor(game_img, cv.COLOR_BGR2GRAY)
        # find the offset here, the template is the tiny gap above the first row
        template = cv.imread("template/board.png", 0)
        m = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)
        board_offset = None
        for loc in zip(*np.where(m >= 0.8)[::-1]):
            board_offset = int(loc[1])
            break

        if board_offset is None:
            print('Failed to find board. Go inside any dungeon to setup properly.')
            exit(-1)
        else:
            print('Get board offset of {}'.format(board_offset))

        take_screenshot({"top": top + board_offset, "left": left, "width": width, "height": height - board_offset}, write2disk=True)
        # board and game location
        with open('game.loc', 'w') as loc:
            loc.write(str(([left, top, left + width, top + height], 
                [left, top + board_offset, left + width, top + height]))) 
    else:
        print('Window not found')
        exit(-1)

def clearAllWindows():
    cv.waitKey()
    cv.destroyAllWindows()

# this check if this script is being executed instead of using as a module
if __name__ == "__main__":
    # get_location_manually()
    get_location_automatically()
