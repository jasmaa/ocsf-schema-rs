import json
import os
import logging
import sys
from pathlib import Path

BASE_DIR = "./data"
OUTPUT_DIR = "./ocsf-schema-rs"


def remove_titles(v):
    if isinstance(v, dict) and "title" in v and isinstance(v["title"], str):
        del v["title"]
    if isinstance(v, dict):
        for k in v.keys():
            remove_titles(v[k])
    elif isinstance(v, list):
        for child in v:
            remove_titles(child)


def generate_all_schema():
    defs = {}

    for type in ["objects", "classes"]:
        type_dir = Path(BASE_DIR).joinpath(type)
        fnames = os.listdir(type_dir)
        for fname in fnames:
            if fname.endswith(".json"):
                def_name = fname.split(".")[0]
                logging.info(f"Processing {def_name}...")
                with open(Path(type_dir).joinpath(fname), "r") as f:
                    schema = json.load(f)
                    # Remove JSON Schema title to avoid name conflicts in typify
                    remove_titles(schema)
                    if "$defs" in schema:
                        del schema["$defs"]
                    defs[def_name] = schema

    all_schema = {
        "$defs": defs,
    }

    output_path = Path(OUTPUT_DIR).joinpath("all.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(all_schema, f)
    logging.info(f"Wrote to {output_path}.")


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    generate_all_schema()
    logging.info("Done!")
