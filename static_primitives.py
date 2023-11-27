class BaseStaticPrimitive:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        input_field_config = {}
        if s.INPUT_FIELD_CONFIG_ID:
            input_field_config = s.INPUT_FIELD_CONFIGS[s.INPUT_FIELD_CONFIG_ID]

        return {
            "required": {
                f"Input_{s.RETURN_TYPES[0]}": (s.RETURN_TYPES[0], input_field_config),
            },
        }
    
    INPUT_FIELD_CONFIGS = {
                "int_field": {
                    "display": "number"
                },
                "float_field": {
                    "display": "number"},
                "string_field": {
                    "multiline": False, 
                },
                "string_field_ml": {
                    "multiline": True, 
                },
                }

    RETURN_TYPES = ("STRING",)
    INPUT_FIELD_CONFIG_ID = None

    FUNCTION = "output"

    CATEGORY = "primitives"

    def output(self, **kwargs):
        return (kwargs[f"Input_{self.RETURN_TYPES[0]}"],)

class StringStaticPrimitive(BaseStaticPrimitive):
    RETURN_TYPES = ("STRING",)
    INPUT_FIELD_CONFIG_ID = "string_field"

class StringMlStaticPrimitive(BaseStaticPrimitive):
    RETURN_TYPES = ("STRING",)
    INPUT_FIELD_CONFIG_ID = "string_field_ml"

class IntStaticPrimitive(BaseStaticPrimitive):
    RETURN_TYPES = ("INT",)
    INPUT_FIELD_CONFIG_ID = "int_field"

class FloatStaticPrimitive(BaseStaticPrimitive):
    RETURN_TYPES = ("FLOAT",)
    INPUT_FIELD_CONFIG_ID = None
    INPUT_FIELD_CONFIG_ID = "float_field"