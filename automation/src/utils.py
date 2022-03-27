"""
Utilities
"""

import time
import os

import mss
import mss.tools

from config import ONE_CYCLE, ORB_COUNT, SCREEN_SCALE
from typing import Tuple, Dict

def waitForNextCycle():
    waitForCycles(1)

def waitForCycles(count: int):
    # at least, one cycle here
    time.sleep((ONE_CYCLE * max(count, 1)) / 1000)

def getExcutableName() -> str:
    if os.name == 'nt':
        return 'pazusoba.exe'
    return 'pazusoba.out'

def getMonitorParamsFrom(board: Tuple[int, int, int, int]) -> Dict[str, int]:
    """
    Get monitor params for taking screenshot from a board based on SCREEN_SCALE
    """
    left, top, _, _ = board
    width, height = getWidthHeightFrom(board)

    return {"top": top * SCREEN_SCALE, "left": left * SCREEN_SCALE, "width": width, "height": height}

def getWidthHeightFrom(board: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """
    Get Width, Height from a board based on SCREEN_SCALE
    """
    left, top, end_left, end_top = board
    width = (end_left - left) * SCREEN_SCALE
    height = (end_top - top) * SCREEN_SCALE
    return (width, height)

def getColumnRow() -> Tuple[int, int]:
    """
    Get Column, Row based on ORB_COUNT
    """
    if ORB_COUNT == 30:
        # 6x5
        return (6, 5)
    elif ORB_COUNT == 42:
        # 7x6
        return (7, 6)
    elif ORB_COUNT == 20:
        # 5x4
        return (5, 4)
    else:
        exit("=> Unknown orb count (only support 20, 30 and 42)")

def take_screenshot(monitor, write2disk=False, name="output.png"):
    # # NOTE: move the cursor outside the game screen so that it doesn't cover up the screen
    # x = monitor["height"] / 2 + monitor["top"]
    # y = monitor["width"] + monitor["left"] + 10
    # pyautogui.moveTo(y, y)

    with mss.mss() as screenshot:
        screen_raw = screenshot.grab(monitor)
        # Save to disk TODO: is this still necessary
        if write2disk:
            mss.tools.to_png(screen_raw.rgb, screen_raw.size, output=name)
        return screen_raw
