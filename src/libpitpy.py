from typing import List, Dict
from benchmark import time_it


@time_it("PYTHON")
def print_function():
    print("Hello from Python!")

@time_it("PYTHON")
def return_function():
    return 42

@time_it("PYTHON")
def compute_heavy_function_with_return(n: int):
    count = 0
    for i in range(n): 
        if i % 3 == 0:
            count += 1
        if i % 5 == 0:
            count -= 1;
    return count

@time_it("PYTHON")
def iter_over_list(l: List):
    for e in l:
        print(e)

@time_it("PYTHON")
def iter_over_list_of_dict(l: List[Dict]):
    for e in l:
        print(e)
