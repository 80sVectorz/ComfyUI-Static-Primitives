from .static_primitives import *
from .collection_primitives import *
import os, shutil
import folder_paths
import json

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = os.path.dirname(folder_paths.__file__)
application_web_extensions_directory = os.path.join(application_root_directory, "web", "extensions", "StaticPrimitives")

shutil.copytree(module_js_directory, application_web_extensions_directory, dirs_exist_ok=True)

collection_primitives_definitions_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "collection_primitives")

definition_files = [f for f in os.listdir(collection_primitives_definitions_directory) if f.endswith('.json')]
collection_primitives_classes = {}
collection_primitives_node_class_mappings = {}
collection_primitives_node_display_name_mappings = {}

duplicate_counter = {}

for file in definition_files:
    with open(os.path.join(collection_primitives_definitions_directory, file), 'r') as f:
        data = json.load(f)
        for key in data.keys():
            duplicate_counter[key]=0
            if key in collection_primitives_classes.keys():
                duplicate_counter[key]+=1
                continue
            if type(data[key]) is not list or len(data[key]) == 0 or type(data[key][0]) is not str:
                print(f"ComfyUI-Static-Primitives:\n !!Found invalid collection primitive definition with key: {key} skipping!!")
                continue

            new_class = CollectionPrimitiveFactory(key, data[key])
            collection_primitives_classes[key] = new_class
            collection_primitives_node_class_mappings[f"{key}StaticCollectionPrimitive"] = new_class
            collection_primitives_node_display_name_mappings[f"{key}StaticCollectionPrimitive"] = f"Collection Primitive ({key})"

for key, duplicates in duplicate_counter.items():
    if duplicates > 0:
        print(f"ComfyUI-Static-Primitives:\n !!Found {duplicates+1} definitions using the same key: {key} skipping all!!")
        collection_primitives_classes.remove(key)
        collection_primitives_node_class_mappings.remove(f"{key}StaticCollectionPrimitive")
        collection_primitives_node_display_name_mappings.remove(f"{key}StaticCollectionPrimitive")


NODE_CLASS_MAPPINGS = {
    "StringStaticPrimitive": StringStaticPrimitive,
    "StringMlStaticPrimitive": StringMlStaticPrimitive,
    "IntStaticPrimitive": IntStaticPrimitive,
    "FloatStaticPrimitive": FloatStaticPrimitive,
}
NODE_CLASS_MAPPINGS.update(collection_primitives_node_class_mappings)

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringStaticPrimitive": "Primitive (STRING)",
    "StringMlStaticPrimitive": "Primitive (STRING MULTI-LINE)",
    "IntStaticPrimitive": "Primitive (INT)",
    "FloatStaticPrimitive": "Primitive (FLOAT)",
}
NODE_DISPLAY_NAME_MAPPINGS.update(collection_primitives_node_display_name_mappings)
