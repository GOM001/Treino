import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Final.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "python web scraper",
    version = "1.0",
    description = "...",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
