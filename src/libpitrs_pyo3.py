import sys
sys.path.append("../target/release")

import libpit
from typing import List
from benchmark import time_it



@time_it(name="RUST CLASSIC IMPORT")
def print_function():
    libpit.print_function_classic_import()

@time_it(name="RUST CLASSIC IMPORT")
def return_function():
    return libpit.return_function_classic_import()

@time_it(name="RUST CLASSIC IMPORT")
def compute_heavy_function_with_return(n: int):
    return libpit.compute_heavy_function_with_return_classic_import(n)

@time_it(name="RUST CLASSIC IMPORT")
def iter_over_list(l: List):
    return libpit.iter_over_list(l)

