# Call rust from python

Results so far

```
------------------------------
> STARTING RUST print_function
Hello from Rust!
> ELAPSED TIME: 0:00:00.000093
------------------------------
> STARTING PYTHON print_function
Hello from Python!
> ELAPSED TIME: 0:00:00.000003
------------------------------
> STARTING RUST CLASSIC IMPORT print_function
Hello from Rust! Classic import
> ELAPSED TIME: 0:00:00.000003
------------------------------
> STARTING RUST return_function
> ELAPSED TIME: 0:00:00.000033
Original value: 42, plus one: 43
------------------------------
> STARTING PYTHON return_function
> ELAPSED TIME: 0:00:00.000001
Original value: 42, plus one: 43
------------------------------
> STARTING RUST CLASSIC IMPORT return_function
> ELAPSED TIME: 0:00:00.000001
Original value: 42, plus one: 43
------------------------------
> STARTING RUST compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.013815
Heavy computation 1333334
------------------------------
> STARTING PYTHON compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.545133
Heavy computation 1333334
------------------------------
> STARTING RUST CLASSIC IMPORT compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.013675
Heavy computation 1333334
------------------------------
> STARTING RUST WITH PYTHON FOR LOOP compute_heavy_function_with_return_and_for_loop_outside
> ELAPSED TIME: 0:00:01.696763
Heavy computation with python for loop 1333334
------------------------------
> STARTING RUST LOOP OUTSIDE compute_for_loop_outside
> ELAPSED TIME: 0:00:01.268818
For loop outside 420000000
------------------------------
> STARTING RUST LOOP INSIDE compute_for_loop_inside
> ELAPSED TIME: 0:00:00.000069
For loop inside 420000000
------------------------------
> STARTING PYTHON iter_over_list
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
> ELAPSED TIME: 0:00:00.000045
------------------------------
> STARTING RUST CLASSIC IMPORT iter_over_list
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
> ELAPSED TIME: 0:00:00.000039

```
