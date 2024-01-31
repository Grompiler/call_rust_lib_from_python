import libpitrs_pyo3 as pyo3
import libpitpy as py
from libpitrs import Abi

rs = Abi()


rs.print_function()
py.print_function()
pyo3.print_function()


r = rs.return_function()
print(f"Original value: {r}, plus one: {r+1}")

r = py.return_function()
print(f"Original value: {r}, plus one: {r+1}")

r = pyo3.return_function()
print(f"Original value: {r}, plus one: {r+1}")


N = 100_000_00
r = rs.compute_heavy_function_with_return(N)
print(f"Heavy computation {r}")

r = py.compute_heavy_function_with_return(N)
print(f"Heavy computation {r}")

r = pyo3.compute_heavy_function_with_return(N)
print(f"Heavy computation {r}")


r = rs.compute_heavy_function_with_return_and_for_loop_outside(N)
print(f"Heavy computation with python for loop {r}")


r = rs.compute_for_loop_outside(N)
print(f"For loop outside {r}")

r = rs.compute_for_loop_inside(N)
print(f"For loop inside {r}")


l = list(range(20))
py.iter_over_list(l)
pyo3.iter_over_list(l)
