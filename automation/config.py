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

# read location from game.loc
import os
if os.path.exists('game.loc'):
    with open('game.loc', 'r') as loc:
        last_location = eval(loc.read())

    (game, board) = last_location
    if (game is None) or (board is None):
        print('Failed to reading locations')
        exit(-1)
    else:
        GAME_LOCATION  = game
        BOARD_LOCATION = board
else:
    print("Setup game location first with location.py")
    exit(-1)

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
