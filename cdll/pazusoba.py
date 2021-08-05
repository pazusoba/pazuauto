"""
Call methods exported in the shared library
"""
from ctypes import *
from typing import List
import os


class CRoute(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("size", c_int)]


class Route:
    """
    Convert C Route to Python Object. 
    NOTE: not necessary, use if this doesn't affect the performance
    """
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


libpazusoba = CDLL("../automation/pazusoba.so", winmode=0)
# NOTE: the restype here must be correct to call it properly
libpazusoba.solve.restype = POINTER(CRoute)
libpazusoba.solve.argtypes = (c_int, POINTER(c_char_p))
libpazusoba.freeRoute.restype = None
libpazusoba.freeRoute.argtypes = [POINTER(CRoute)]


def solve(arguments: List[str]) -> List[Route]:
    # additional step is required here because Mac is stricter than Windows
    argv = []
    for s in arguments:
        argv.append(c_char_p(s.encode('ascii')))
        # argv.append(create_string_buffer(s.encode('ascii')))
    c_argc = len(arguments)
    c_argv = (c_char_p * c_argc)()
    c_argv[:] = argv

    routes_cpp = libpazusoba.solve(c_argc, c_argv)
    if routes_cpp is None:
        return []
    else:
        size = routes_cpp[0].size
        routes = []
        for i in range(size):
            r = routes_cpp[i]
            routes.append(Route(r.x, r.y))
        freeList(routes_cpp)
        return routes


def freeList(routes: POINTER(CRoute)):
    libpazusoba.freeRoute(routes)


if __name__ == '__main__':
    route = solve(
        ["pazusoba.so", "RHLBDGPRHDRJPJRHHJGRDRHLGLPHBB", "3", "50", "10000"])
    length = len(route)
    print("There are {} steps.\n{}".format(length, route))
