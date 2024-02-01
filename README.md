# Call rust from python

Results so far

```
------------------------------
> STARTING RUST print_function
Hello from Rust!
> ELAPSED TIME: 0:00:00.000072
------------------------------
> STARTING PYTHON print_function
Hello from Python!
> ELAPSED TIME: 0:00:00.000006
------------------------------
> STARTING RUST CLASSIC IMPORT print_function
Hello from Rust! Classic import
> ELAPSED TIME: 0:00:00.000005
------------------------------
> STARTING RUST return_function
> ELAPSED TIME: 0:00:00.000051
Original value: 42, plus one: 43
------------------------------
> STARTING PYTHON return_function
> ELAPSED TIME: 0:00:00.000002
Original value: 42, plus one: 43
------------------------------
> STARTING RUST CLASSIC IMPORT return_function
> ELAPSED TIME: 0:00:00.000002
Original value: 42, plus one: 43
------------------------------
> STARTING RUST compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.135534
Heavy computation 13333334
------------------------------
> STARTING PYTHON compute_heavy_function_with_return
> ELAPSED TIME: 0:00:05.584844
Heavy computation 13333334
------------------------------
> STARTING RUST CLASSIC IMPORT compute_heavy_function_with_return
> ELAPSED TIME: 0:00:00.134142
Heavy computation 13333334
------------------------------
> STARTING RUST WITH PYTHON FOR LOOP compute_heavy_function_with_return_and_for_loop_outside
> ELAPSED TIME: 0:00:16.895703
Heavy computation with python for loop 13333334
------------------------------
> STARTING RUST LOOP OUTSIDE compute_for_loop_outside
> ELAPSED TIME: 0:00:13.188121
For loop outside 4200000000
------------------------------
> STARTING RUST LOOP INSIDE compute_for_loop_inside
> ELAPSED TIME: 0:00:00.000061
For loop inside -94967296
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
> ELAPSED TIME: 0:00:00.000074
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
> ELAPSED TIME: 0:00:00.000063
------------------------------
> STARTING PYTHON iter_over_list_of_dict
{'a': 1, 'b': 2}
{'b': 2}
{'c': 3}
{'d': 4}
> ELAPSED TIME: 0:00:00.000027
------------------------------
> STARTING RUST CLASSIC IMPORT iter_over_list_of_dict
{'a': 1, 'b': 2}
{'b': 2}
{'c': 3}
{'d': 4}
> ELAPSED TIME: 0:00:00.000008

```
