import os
import json

class CascadeResolutions:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        cls.size_sizes, cls.size_dict = read_sizes()
        return {
            'required': {
                'size_selected': (cls.size_sizes,), 
                'multiply_factor': ("INT", "FLOAT")
            }
        }

    RETURN_TYPES = ( "INT", "INT")
    RETURN_NAMES = ( "width", "height")
    FUNCTION = "return_res"
    OUTPUT_NODE = True
    CATEGORY = "Resolution"

    def return_res(self, size_selected, multiply_factor):
        # Extract resolution name and dimensions using the key
        selected_info = self.size_dict[size_selected]
        width = selected_info["width"] * multiply_factor
        height = selected_info["height"] * multiply_factor
        name = selected_info["name"]
        return (width, height,name)

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
    size_sizes = [f"{key} - {value['name']}" for key, value in data['sizes'].items()]
    size_dict = {f"{key} - {value['name']}": value for key, value in data['sizes'].items()}
    return size_sizes, size_dict
