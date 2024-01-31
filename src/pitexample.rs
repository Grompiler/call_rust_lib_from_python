use pyo3::types::PyList;
use pyo3::{prelude::*, wrap_pyfunction};

#[pyfunction]
fn print_function_classic_import() {
    println!("Hello from Rust! Classic import");
}

#[pyfunction]
fn return_function_classic_import() -> i32 {
    42
}

#[pyfunction]
fn compute_heavy_function_with_return_classic_import(n: usize) -> i32 {
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

#[pyfunction]
fn iter_over_list(l: &PyList) {
    for i in l {
        println!("{i}");
    }
}

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pymodule]
fn libpit(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(sum_as_string))?;
    m.add_wrapped(wrap_pyfunction!(print_function_classic_import))?;
    m.add_wrapped(wrap_pyfunction!(return_function_classic_import))?;
    m.add_wrapped(wrap_pyfunction!(
        compute_heavy_function_with_return_classic_import
    ))?;
    m.add_wrapped(wrap_pyfunction!(iter_over_list))?;

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
