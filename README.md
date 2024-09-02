# OCSF Schema

[![Crates.io Version](https://img.shields.io/crates/v/ocsf-schema-rs)
](https://crates.io/crates/ocsf-schema-rs)

Unofficial OCSF data types for Rust based on OCSF JSON Schema.

## Getting started

Install with:

```
cargo add ocsf-schema-rs
```

### Usage

Data types are generated using
[Typify](https://github.com/oxidecomputer/typify). Structs can be constructed
either manually:

```rust
let g = Group {
    type_: None,
    desc: None,
    domain: None,
    name: Some(String::from("My Group")),
    privileges: vec![],
    uid: None,
};
```

or with builder:

```rust
let g: Group = Group::builder()
    .name(String::from("My Group"))
    .try_into()
    .unwrap();
```


## Development

Install deps:

```
pip install -r scripts/requirements.txt
```

Download OCSF JSON Schema:

```
python scripts/download_schemas.py
python scripts/generate_all_schema.py
```

Build ocsf-schema-rs

```
cd ocsf-schema-rs
cargo build
```

## Compatibility

| ocsf-schema-rs | OCSF  |
|----------------|-------|
| 0.1.0-alpha    | 1.3.0 |