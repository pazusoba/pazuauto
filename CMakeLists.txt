cmake_minimum_required (VERSION 3.10)

project(
    pazuauto
    VERSION 0.8.0
    HOMEPAGE_URL https://github.com/HenryQuan/pazuauto
    DESCRIPTION "Automate Puzzle & Dragons with the power of pazusoba"
)

add_subdirectory(pazusoba EXCLUDE_FROM_ALL)
# rename pazusoba_release to pazusoba, update output
set_target_properties(
    pazusoba_release
    PROPERTIES 
    OUTPUT_NAME "pazusoba"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/automation"
)
