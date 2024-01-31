# call_rust_lib_from_python

Results so far

```
------------------------------
> STARTING RUST print_function
Hello from Rust!
> ELAPSED TIME: 0:00:00.000099
------------------------------
> STARTING PYTHON print_function
Hello from Python!
> ELAPSED TIME: 0:00:00.000003
------------------------------
> STARTING RUST return_function
> ELAPSED TIME: 0:00:00.000044
Original value: 42, plus one: 43
------------------------------
> STARTING PYTHON return_function
> ELAPSED TIME: 0:00:00
Original value: 42, plus one: 43
------------------------------
> STARTING RUST compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.013589
Heavy computation 1333334
------------------------------
> STARTING PYTHON compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.571714
Heavy computation 1333334
------------------------------
> STARTING RUST WITH PYTHON FOR LOOP compute_heavy_function_with_return_and_for_loop_outside
> ELAPSED TIME: 0:00:01.699847
Heavy computation with python for loop 1333334
------------------------------
> STARTING RUST LOOP OUTSIDE compute_for_loop_outside
> ELAPSED TIME: 0:00:01.267169
For loop outside 420000000
------------------------------
> STARTING RUST LOOP INSIDE compute_for_loop_inside
> ELAPSED TIME: 0:00:00.000086
For loop inside 420000000

```
