use ocsf_schema_rs::{Authentication, Group, User, Actor};
use std::fs;

fn main() {
    let contents = fs::read_to_string("./data.json").unwrap();
    let data: Actor = serde_json::from_str(contents.as_str()).unwrap();

    println!("{:?}", data)
}
