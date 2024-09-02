import json
import os
import pathlib


def remove_titles(v):
    if isinstance(v, dict) and "title" in v and isinstance(v["title"], str):
        del v["title"]
    if isinstance(v, dict):
        for k in v.keys():
            remove_titles(v[k])
    elif isinstance(v, list):
        for child in v:
            remove_titles(child)


defs = {}

OBJECTS_BASE_DIR = "./data/objects"
fnames = os.listdir(OBJECTS_BASE_DIR)
for fname in fnames:
    if fname.endswith(".json"):
        def_name = fname.split(".")[0]
        with open(pathlib.Path(OBJECTS_BASE_DIR).joinpath(fname), "r") as f:
            schema = json.load(f)
            # Remove JSON Schema title to avoid name conflicts in typify
            remove_titles(schema)
            if "$defs" in schema:
                del schema["$defs"]
            defs[def_name] = schema

CLASSES_BASE_DIR = "./data/classes"
fnames = os.listdir(CLASSES_BASE_DIR)
for fname in fnames:
    if fname.endswith(".json"):
        def_name = fname.split(".")[0]
        with open(pathlib.Path(CLASSES_BASE_DIR).joinpath(fname), "r") as f:
            schema = json.load(f)
            # Remove JSON Schema title to avoid name conflicts in typify
            remove_titles(schema)
            if "$defs" in schema:
                del schema["$defs"]
            defs[def_name] = schema


all_schema = {
    "$defs": defs,
    "allOf": [
        {
            "$ref": f"#/$defs/{k}"
        } for k in defs.keys()
    ]
}

with open("./data/all.json", "w") as f:
    json.dump(all_schema, f)
