# call_rust_lib_from_python

Results so far

```
------------------------------
> STARTING RS print_function
Hello from Rust!
> ELAPSED TIME: 0:00:00.000069
------------------------------
> STARTING PY print_function
Hello from Python!
> ELAPSED TIME: 0:00:00.000003
------------------------------
> STARTING RS return_function
> ELAPSED TIME: 0:00:00.000032
Original value: 42, plus one: 43
------------------------------
> STARTING PY return_function
> ELAPSED TIME: 0:00:00.000001
Original value: 42, plus one: 43
------------------------------
> STARTING RS compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.134674
Heavy computation 13333334
------------------------------
> STARTING PY compute_heavy_function_with_return
> ELAPSED TIME: 0:00:05.363475
Heavy computation 13333334

```
