"""
Configurations for the automation (static and dynamic)
"""

# TODO: Everything should be moved to a class instead of using globals 
# They are all captical so it is easy to extract them from methods

# # # # # # # # # # # #
#
# CONSTANTS
# Modify them before running
#
# # # # # # # # # # # #

# The cycle of automation
ONE_CYCLE = 500

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
        if (w > 1 or h > 1):
            print("Window %s:" % window_name)
            print("\tLocation: (%d, %d)" % (x, y))
            print("\t    Size: (%d, %d)" % (w, h))
            print(rect)

            take_screenshot({"top": y + 58, "left": x + 118, "width": w - 140, "height": h - 90}, write2disk=True)

win32gui.EnumWindows(enumHandler, None)

# Game is the entire game without status bar
# Board is only the board area
GAME_LOCATION  = [1897, 149, 2536, 1265]
BOARD_LOCATION = [1896, 730, 2535, 1263]


# When in DEBUG mode, more texts will be printed
DEBUG_MODE = True

# These values shouldn't be changed
ORB_TEMPLATE_SIZE = (140, 140)
BOARD_UNIFORM_SIZE = (830, 690)

# Resize for game ratio 2:1, 16:9 and 3:2
GAME_SCREEN_SIZE_2_1  = (1000, 1950)
GAME_SCREEN_SIZE_16_9 = (1000, 1720)
GAME_SCREEN_SIZE_3_2  = (1000, 1440)

# On Mac OS, the scale might be 2 instead of 1 because of the retina display
SCREEN_SCALE = 1

# Added paddings to images
BORDER_LENGTH = 1

# This is used to ignore similar matches by how close they are using this offset
SORT_OFFSET = 100

# 20, 30 or 42
ORB_COUNT = 30
