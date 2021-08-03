"""
Call methods exported in the shared library
"""
from ctypes import *
import os

# mac only for now, need to rename to libpazuosba.so
libpazusoba = CDLL("../build/pazusoba/libpazusoba.dylib", winmode=0)

libpazusoba.solve.restype = POINTER(c_int)
libpazusoba.solve.argtypes = (POINTER(c_int), c_int)


def solve(argc, argv: list):
    pass


if __name__ == '__main__':
    route = solve(4, ["RHLBDGPRHDRJPJRHHJGRDRHLGLPHBB", "3", "50", "10000"])
    print(route)
