use std::io::{BufWriter, Write};

use ocsf_schema_rs::{Actor, Cloud, Device, File, FileActivity, Metadata, Product};

fn main() {
    // Construct FileActivity log
    // This is a sample log event for creating a file called `hello_world.txt`.
    let actor: Actor = Actor::builder().try_into().unwrap();
    let device: Device = Device::builder().type_id(1).try_into().unwrap();
    let cloud: Cloud = Cloud::builder().provider("AWS").try_into().unwrap();
    let f: File = File::builder()
        .name("hello_world.txt")
        .type_id(1)
        .try_into()
        .unwrap();
    let product: Product = Product::builder()
        .vendor_name("Alter Ego")
        .try_into()
        .unwrap();
    let metadata: Metadata = Metadata::builder()
        .product(product)
        .version("1.3.0")
        .try_into()
        .unwrap();

    let class_uid = 1001;
    let activity_id = 1;
    let file_activity: FileActivity = FileActivity::builder()
        .activity_id(activity_id)
        .action_id(0)
        .actor(actor)
        .category_uid(1)
        .class_uid(class_uid)
        .device(device)
        .time(0)
        .file(f)
        .metadata(metadata)
        .severity_id(1)
        .type_uid(class_uid * 100 + activity_id)
        .cloud(cloud)
        .osint(vec![])
        .try_into()
        .unwrap();

    // Serialize and write log to file
    let file = std::fs::File::create("sample.json").unwrap();
    let mut writer = BufWriter::new(file);
    serde_json::to_writer_pretty(&mut writer, &file_activity).unwrap();
    writer.flush().unwrap();
}
