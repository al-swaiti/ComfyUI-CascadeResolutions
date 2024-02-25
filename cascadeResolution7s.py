import os
import json

class CascadeResolutions:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        s.size_sizes, s.size_dict = read_sizes()
        return {'required': {
                    'size_selected': (s.size_sizes,), 
                    'multiply_factor': ("INT", "FLOAT")
                }
        }

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("width","height")
    FUNCTION = "return_res"
    OUTPUT_NODE = True
    CATEGORY = "Resolution"

    def return_res(self, size_selected, multiply_factor):
        # Extract just the key part for lookup
        key = size_selected.split(" (")[0]
        width = self.size_dict[key]["width"] * multiply_factor
        height = self.size_dict[key]["height"] * multiply_factor
        return (width, height)

NODE_CLASS_MAPPINGS = {
    "CascadeResolutions": CascadeResolutions
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CascadeResolutions": "Cascade Resolutions"
}

def read_sizes():
    p = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(p, 'sizes.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    size_sizes = [f"{key} ({value['name']})" for key, value in data['sizes'].items()]
    size_dict = {key: value for key, value in data['sizes'].items()}
    return size_sizes, size_dict