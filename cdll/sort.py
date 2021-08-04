from ctypes import *
from typing import List
import os

# https://stackoverflow.com/a/64472088
# winmode 0 is working here and it is required
libsort = CDLL("./build/libsort.so", winmode=0)

# https://stackoverflow.com/a/29025380
libsort.sortArray.restype = POINTER(c_int)
libsort.sortArray.argtypes = (POINTER(c_int), c_int)


def sort_array(array) -> List[int]:
    size = len(array)
    C_INT_ARRAY = (c_int * size)
    # convert to C int array with size
    c_array = C_INT_ARRAY(*array)
    c_pointer = libsort.sortArray(c_array, size)
    # here, c_pointer works like a list so can simply copy it
    print(c_pointer[:size])
    return list(c_array)


if __name__ == '__main__':
    array = [123, 54, 213, 5, 93, 956, 370, 58, 164,
             38, 69, 1000, 20000, 35321, 58719325, 21438021]
    sorted_array = sort_array(array)
    print(sorted_array)
