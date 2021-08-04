cmake_minimum_required (VERSION 3.10)

project(
    cdll
    DESCRIPTION "Call C++ code from Python"
)

# use a uniform name
set(CMAKE_SHARED_LIBRARY_SUFFIX ".so")

# sort a python list in C++
add_library(
    sort SHARED
    sort.cpp
)
add_custom_command(
    TARGET sort
    COMMENT "Test sort"
    POST_BUILD 
    COMMAND python3 sort.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
)

# return a C/C++ struct to python
add_library(
    class SHARED
    class.cpp
)
add_custom_command(
    TARGET class
    COMMENT "Test class"
    POST_BUILD 
    COMMAND python3 class.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
)
