use std::thread;


#[no_mangle]
pub extern fn process() {
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(|| {
            let mut x = 0;
            for _ in 0..5000000 {
                x += 1
            }
            x
        })
    }).collect();

    for h in handles {
        println!("Thread finished with count={}",
                 h.join().map_err(|_| "Could not join a thread!").unwrap());
    }
    println!("done from Rust!");
}

#[no_mangle]
fn process_not_pub() {
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(|| {
            let mut x = 0;
            for _ in 0..5000000 {
                x += 1
            }
            x
        })
    }).collect();

    for h in handles {
        println!("Thread finished with count={}",
                 h.join().map_err(|_| "Could not join a thread!").unwrap());
    }
    println!("done from Rust not pub and not extern!");
}
