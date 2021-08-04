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
libpazusoba.solve.restype = Route
libpazusoba.solve.argtypes = (c_int, POINTER(c_char_p))
# have a look, https://stackoverflow.com/a/24061473


def solve(arguments: List[str]) -> Route:
    # additional step is required here because Mac is stricter than Windows
    argv = []
    for s in arguments:
        argv.append(c_char_p(s.encode('ascii')))
        # argv.append(create_string_buffer(s.encode('ascii')))
    print(argv)
    c_argc = len(arguments)
    c_argv = (c_char_p * c_argc)()
    c_argv[:] = argv
    print(c_argv._objects)
    return libpazusoba.solve(c_argc, c_argv)


if __name__ == '__main__':
    route = solve(["", "RHLBDGPRHDRJPJRHHJGRDRHLGLPHBB", "3", "50", "10000"])
    print(route)
