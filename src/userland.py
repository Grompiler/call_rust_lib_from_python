from libpitrs import Abi
import libpitpy as py


rs = Abi()

rs.print_function()

py.print_function()


r = rs.return_function()
print(f"Original value: {r}, plus one: {r+1}")

r = py.return_function()
print(f"Original value: {r}, plus one: {r+1}")


N = 100_000_000
r = rs.compute_heavy_function_with_return(N)
print(f"Heavy computation {r}")

r = py.compute_heavy_function_with_return(N)
print(f"Heavy computation {r}")


