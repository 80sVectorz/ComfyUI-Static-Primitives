from .static_primitives import *
import os, shutil
import folder_paths

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = os.path.dirname(folder_paths.__file__)
application_web_extensions_directory = os.path.join(application_root_directory, "web", "extensions", "StaticPrimitives")

shutil.copytree(module_js_directory, application_web_extensions_directory, dirs_exist_ok=True)

NODE_CLASS_MAPPINGS = {
    "StringStaticPrimitive": StringStaticPrimitive,
    "StringMlStaticPrimitive": StringMlStaticPrimitive,
    "IntStaticPrimitive": IntStaticPrimitive,
    "FloatStaticPrimitive": FloatStaticPrimitive,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "StringStaticPrimitive": "Primitive (STRING)",
    "StringMlStaticPrimitive": "Primitive (STRING MULTI-LINE)",
    "IntStaticPrimitive": "Primitive (INT)",
    "FloatStaticPrimitive": "Primitive (FLOAT)",
}
