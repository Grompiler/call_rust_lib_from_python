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
