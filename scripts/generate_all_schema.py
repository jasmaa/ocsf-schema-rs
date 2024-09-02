import json
import os
import pathlib

defs = {}

OBJECTS_BASE_DIR = "./data/objects"
fnames = os.listdir(OBJECTS_BASE_DIR)
for fname in fnames:
    if fname.endswith(".json"):
        def_name = fname.split(".")[0]
        with open(pathlib.Path(OBJECTS_BASE_DIR).joinpath(fname), "r") as f:
            schema = json.load(f)
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
