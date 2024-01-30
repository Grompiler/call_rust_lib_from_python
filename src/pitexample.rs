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
