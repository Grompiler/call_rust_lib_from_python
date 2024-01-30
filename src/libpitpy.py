from typing import Dict, List
from benchmark import time_it_py


@time_it_py
def print_function():
    print("Hello from Python!")

@time_it_py
def return_function():
    return 42

@time_it_py
def compute_heavy_function_with_return(n: int):
    count = 0
    for i in range(n): 
        if i % 3 == 0:
            count += 1
        if i % 5 == 0:
            count -= 1;
    return count

@time_it_py
def function_with_parameters_and_return(an_integer: int, a_str: str, a_list: List, a_dict: Dict):
    return None


