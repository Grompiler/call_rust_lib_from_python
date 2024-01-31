from ctypes import cdll
from cffi import FFI
from threading import Lock, Thread
from typing import Dict, List
from benchmark import time_it_rs


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Abi(metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        self.define_ffi_interface()
        self.load_lib()

    def define_ffi_interface(self):
        self.ffi = FFI()
        self.ffi.cdef("void print_function();")
        self.ffi.cdef("int return_function();")
        self.ffi.cdef("int compute_heavy_function_with_return(unsigned long);")
        # self.ffi.cdef('int compute_heavy_function_with_return(int);')

    def load_lib(self):
        self._lib = self.ffi.dlopen("../target/release/libpit.so")

    @time_it_rs
    def print_function(self):
        self._lib.print_function()

    @time_it_rs
    def return_function(self):
        return self._lib.return_function()

    @time_it_rs
    def compute_heavy_function_with_return(self, n: int):
        return self._lib.compute_heavy_function_with_return(n)

    # @time_it_rs
    # @staticmethod
    # def function_with_parameters_and_return(an_integer: int, a_str: str, a_list: List, a_dict: Dict):
    #     return _LIB.function_with_parameters_and_return(an_integer, a_str, a_list, a_dict)
    #
