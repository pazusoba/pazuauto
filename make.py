import platform, os, sys
import shutil

def make():
    extra_flags = ""
    if platform.system() == "Windows":
        # for now, MinGW should be used, MSVC may be supported in the future
        extra_flags = '-G "MinGW Makefiles"'
    os.system("cmake -B build {}".format(extra_flags))
    os.system("cmake --build build --target pazuauto")

    print("See CMakeLists.txt for all targets")

def clean():
    _clean("build")

def _clean(folder: str):
    if os.path.exists(folder):
        shutil.rmtree(folder)

def experiment():
    if platform.system() == "Windows":
        os.system("cd pazusoba/experiment && mingw32-make so")
        os.system("move .\pazusoba\experiment\libpazusoba.so .\\automation\\")
    else:
        os.system("cd pazusoba/experiment && make so")
        os.system("mv pazusoba/experiment/libpazusoba.so automation/")

argv = sys.argv
argc = len(argv)
if argc <= 1:
    make()
elif argc == 2:
    option = argv[1]
    if option == "clean":
        clean()
    if option == "experiment":
        experiment()
    else:
        exit("Unknown command - (clean) avilable")
