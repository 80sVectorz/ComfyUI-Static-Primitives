
class BaseCollectionPrimitive:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                f"Input_{s.COLLECTION_TYPE}": (s.RETURN_TYPES[0],),
            },
        }
    
    COLLECTION_TYPE = None
    
    RETURN_TYPES = ([],)
    INPUT_FIELD_CONFIG_ID = None

    FUNCTION = "output"

    CATEGORY = "primitives"

    def output(self, **kwargs):
        return (kwargs[f"Input_{self.COLLECTION_TYPE}"],)

def CollectionPrimitiveFactory(key,collection):
    def __init__(self, **kwargs):
        BaseCollectionPrimitive.__init__(self)

    new_class = type(f"{key}StaticCollectionPrimitive", (BaseCollectionPrimitive,),{"__init__": __init__})
    new_class.COLLECTION_TYPE = key 
    new_class.RETURN_TYPES = (collection,)
    return new_class