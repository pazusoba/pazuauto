"""
Call methods exported in the shared library
"""
from ctypes import *
from typing import List
import os


class Route(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("size", c_int)]


# mac only for now, need to rename to libpazuosba.so
libpazusoba = CDLL("../build/pazusoba/libpazusoba.dylib", winmode=0)

libpazusoba.solve.restype = None
libpazusoba.solve.argtypes = (c_int, POINTER(POINTER(c_char)))


def solve(arguments: List[str]) -> Route:
    byte_argv = bytearray()
    size = 0
    for s in arguments:
        b = bytearray(s, 'utf-8')
        byte_argv += b
        size += len(b)
    print(byte_argv)
    argv = (c_char * (size + 1))(*byte_argv)
    argc: int = len(arguments) + 1
    return libpazusoba.solve(argc, argv)


if __name__ == '__main__':
    route = solve(
        ["pazusoba", "RHLBDGPRHDRJPJRHHJGRDRHLGLPHBB", "3", "50", "10000"])
    print(route)
