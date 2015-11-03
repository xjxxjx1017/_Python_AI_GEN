import sys
from cx_Freeze import setup, Executable

## from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

executable = [Executable("main.py", base=base)]

setup(  name = "main",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = executable)