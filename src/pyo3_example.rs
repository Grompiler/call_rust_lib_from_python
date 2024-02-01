use pyo3::types::{PyDict, PyList};
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

#[pyfunction]
fn iter_over_list_of_dict(l: &PyList) {
    for i in l {
        println!("{i}");
    }
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
    m.add_wrapped(wrap_pyfunction!(iter_over_list_of_dict))?;

    Ok(())
}
