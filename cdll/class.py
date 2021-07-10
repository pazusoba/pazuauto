from ctypes import *
import os

class Route(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("size", c_int)]


libclass = CDLL("./build/libclass.so", winmode=0)

libclass.getRoute.restype = POINTER(Route)
libclass.getRoute.argtypes = None

def get_route() -> list:
    routes = libclass.getRoute()
    return routes

def free(routes):
    libclass.freeRoutes(routes)

if __name__ == '__main__':
    routes = get_route()
    size = routes[0].size
    for i in range(size):
        print(routes[i].x, routes[i].y, routes[i].size)
    free(routes)
