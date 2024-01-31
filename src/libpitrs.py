from cffi import FFI
from threading import Lock, Thread
from typing import Dict, List
from benchmark import time_it


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
        self.ffi.cdef("int compute_heavy_function_with_return_and_for_loop_outside(int);")
        self.ffi.cdef("int compute_for_loop_outside();")
        self.ffi.cdef("int compute_for_loop_inside(int);")

    def load_lib(self):
        self._lib = self.ffi.dlopen("../target/release/libpit.so")

    @time_it(name="RUST")
    def print_function(self):
        self._lib.print_function()

    @time_it(name="RUST")
    def return_function(self):
        return self._lib.return_function()

    @time_it(name="RUST")
    def compute_heavy_function_with_return(self, n: int):
        return self._lib.compute_heavy_function_with_return(n)

    @time_it(name="RUST WITH PYTHON FOR LOOP")
    def compute_heavy_function_with_return_and_for_loop_outside(self, n: int):
        count = 0
        for i in range(n): 
            count += self._lib.compute_heavy_function_with_return_and_for_loop_outside(i)
        return count

    @time_it(name="RUST LOOP OUTSIDE")
    def compute_for_loop_outside(self, n: int):
        s = 0
        for i in range(n):
            s += self._lib.compute_for_loop_outside()
        return s

    @time_it(name="RUST LOOP INSIDE")
    def compute_for_loop_inside(self, n: int):
        return self._lib.compute_for_loop_inside(n)
