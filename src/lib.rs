use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn say_hello() {
    println!("say hello b*tch from Rust!");
}

#[pymodule]
fn denilson_fib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    let _ = m.add_wrapped(wrap_pyfunction!(say_hello));
    Ok(())
}
