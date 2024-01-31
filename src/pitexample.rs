use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
/// Formats the sum of two numbers as string
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// This module is a python module implemented in Rust.
#[pymodule]
fn libpit(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;

    Ok(())
}

#[no_mangle]
pub extern "C" fn print_function() {
    println!("Hello from Rust!");
}

#[no_mangle]
pub extern "C" fn return_function() -> i32 {
    42
}

#[no_mangle]
pub extern "C" fn compute_heavy_function_with_return(n: usize) -> i32 {
    let mut count = 0;
    for i in 0..n {
        if i % 3 == 0 {
            count += 1;
        }
        if i % 5 == 0 {
            count -= 1;
        }
    }
    count
}

#[no_mangle]
pub extern "C" fn compute_heavy_function_with_return_and_for_loop_outside(i: i32) -> i32 {
    let mut c = 0;
    if i % 3 == 0 {
        c += 1;
    }
    if i % 5 == 0 {
        c -= 1;
    }
    c
}

#[no_mangle]
pub extern "C" fn compute_for_loop_outside() -> i32 {
    42
}

#[no_mangle]
pub extern "C" fn compute_for_loop_inside(n: i32) -> i32 {
    let mut s = 0;
    for _ in 0..n {
        s += 42;
    }
    s
}
