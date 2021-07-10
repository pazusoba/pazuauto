cmake_minimum_required (VERSION 3.10)

project(
    cdll
    DESCRIPTION "Call C++ code from Python"
)

add_library(
    sort SHARED
    library.cpp
)
add_custom_command(
    TARGET sort
    COMMENT "Run main.py"
    POST_BUILD 
    COMMAND python main.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
)