import sys
from cx_Freeze import setup, Executable
from time import sleep
import csv

base = None
executables = [
        Executable("main.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ["csv"],
        include_files = ["tabelaProdutos.csv"],
        excludes = []
)




setup(
    name = "main.py",
    version = "1.0",
    description = "main",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
