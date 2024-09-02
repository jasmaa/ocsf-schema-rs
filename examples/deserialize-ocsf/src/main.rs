use ocsf_schema_rs::Authentication;
use serde::Deserialize;
use serde_json::Value;
use std::fs;

fn main() {
    let contents = fs::read_to_string("./authentication.json").unwrap();

    let mut deserializer = serde_json::Deserializer::from_str(&contents);
    // Disable recursion limit to handle deeply nested structs
    // See also: https://docs.rs/serde_json/latest/serde_json/struct.Deserializer.html#method.disable_recursion_limit
    deserializer.disable_recursion_limit();
    let deserializer = serde_stacker::Deserializer::new(&mut deserializer);
    let value = Value::deserialize(deserializer).unwrap();

    let data: Authentication = serde_json::from_value(value.clone()).unwrap();
    println!("{:?}", data.activity_id);

    carefully_drop_nested_arrays(value);
}

fn carefully_drop_nested_arrays(value: Value) {
    let mut stack = vec![value];
    while let Some(value) = stack.pop() {
        if let Value::Array(array) = value {
            stack.extend(array);
        }
    }
}
