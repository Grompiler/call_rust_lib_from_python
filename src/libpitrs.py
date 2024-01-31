from ctypes import cdll
from cffi import FFI
from typing import Dict, List
from benchmark import time_it_rs

ffi = FFI()
ffi.cdef('void print_function();')
ffi.cdef('int return_function();')
ffi.cdef('int compute_heavy_function_with_return(unsigned long);')
# ffi.cdef('int compute_heavy_function_with_return(int);')


# _LIB = ffi.dlopen("../target/debug/libpit.so")
_LIB = ffi.dlopen("../target/release/libpit.so")

# UNSAFE CASTS
# def _as_f64(num):
#     """ Cast np.float64 for Rust."""
#     return ffi.cast("double", num)
#
# def _as_f64_array(array):
#     """ Cast np.float64 array to a pointer to float 64s."""
#     return ffi.cast("double*", num)

# def _as_usize(num):
#     """ Cast `num` to Rust `usize`."""
#     return ffi.cast("unsigned long", num)

@time_it_rs
def print_function():
    _LIB.print_function()

@time_it_rs
def return_function():
    return _LIB.return_function()

@time_it_rs
def compute_heavy_function_with_return(n: int):
    return _LIB.compute_heavy_function_with_return(n)

@time_it_rs
def function_with_parameters_and_return(an_integer: int, a_str: str, a_list: List, a_dict: Dict):
    return _LIB.function_with_parameters_and_return(an_integer, a_str, a_list, a_dict)


