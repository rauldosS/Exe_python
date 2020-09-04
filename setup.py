import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("program.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)

setup(
    name = "program",
    version = "1.0",
    description = "Program",
    options = dict(build_exe = buildOptions),
    executables = executables
 )