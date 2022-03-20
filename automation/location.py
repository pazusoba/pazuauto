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

    print(
        "Board Location - [{}, {}, {}, {}]".format(one.x, one.y, two.x, two.y))
    return [one.x, one.y, two.x, two.y]


def get_location_automatically():
    """
    Get the board location automatically on the screen
    """
    win32gui.EnumWindows(enumHandler, None)
    if (location != None):
        [x, y, w, h] = location
        if x < 0 or y < 0:
            print("The window is not visible on the screen")
            exit(-1)
        print('Found window at {}'.format(location))
        window_img = np.array(take_screenshot(
            {"top": y, "left": x, "width": w, "height": h}))

        # find the rectangle contour
        gray_window = cv.cvtColor(window_img, cv.COLOR_BGR2GRAY)
        # the interface is white so it is easy to filter out
        _, binary = cv.threshold(gray_window, 254, 255, cv.THRESH_BINARY)

        (contours, _) = cv.findContours(
            binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv.contourArea(contour) > 10000:
                (left, top, width, height) = cv.boundingRect(contour)
                cv.rectangle(window_img, (left, top),
                             (left+width, top+height), (0, 255, 0), 2)
                break

        cv.imshow("Window", window_img)
        cv.waitKey()

        if top == None:
            print("Unable to determine the location of the game")
            exit(-1)

        # adjust it with manual offset because blackhole has additional controls
        # top = y + 58
        # left = x + 118
        # width = w - 140
        # height = h - 90

        game_img = np.array(take_screenshot(
            {"top": top, "left": left, "width": width, "height": height}))
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

        take_screenshot({"top": top + board_offset, "left": left,
                        "width": width, "height": height - board_offset}, write2disk=True)
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
