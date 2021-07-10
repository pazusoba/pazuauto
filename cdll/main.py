from ctypes import *
import os

# https://stackoverflow.com/a/64472088
# winmode 0 is working here and it is required
libsort = CDLL("./build/libsort.dll", winmode=0)

# https://stackoverflow.com/a/29025380
libsort.sortArray.restype = POINTER(c_int)
libsort.sortArray.argtypes = (POINTER(c_int), c_int)

def sort_array(array) -> list:
    size = len(array)
    c_array = (c_int * size)(*array)
    return libsort.sortArray(c_array, size)

if __name__ == '__main__':
    array = [123, 54, 213, 5, 93, 956, 370, 58, 164, 38, 69]
    print(array)
    sort_array(array)
    print(array)
    print("Sorted list is {}".format(sort_array(array)))
