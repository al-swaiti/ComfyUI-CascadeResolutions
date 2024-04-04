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
<<<<<<< HEAD
                'size_selected': (cls.size_sizes,),  # Existing dropdown for predefined sizes
                'multiply_factor': ("INT" ,{"default": 1, "min": 1}),  # Existing multiply factor
                'manual_width': ("INT", {
                    "default": 0,  # Default value indicating it may not be used
                    "min": 0,  # Minimum value
                }),
                'manual_height': ("INT", {
                    "default": 0,  # Default value indicating it may not be used
                    "min": 0,  # Minimum value
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
=======
                'size_selected': (cls.size_sizes,), 
                'multiply_factor': ("FLOAT", {"default": 1, "max": 16, "min": 0.5, "step": 0.1, "display": "number"})
            }
        }

    RETURN_TYPES = ( "INT", "INT")
    RETURN_NAMES = ( "width", "height")
>>>>>>> upstream/main
    FUNCTION = "return_res"
    OUTPUT_NODE = True
    CATEGORY = "Resolution"

<<<<<<< HEAD
    def return_res(self, size_selected, multiply_factor, manual_width, manual_height):
        # Initialize width and height from the manual input if provided
        if manual_width > 0 and manual_height > 0:
            width = manual_width * multiply_factor
            height = manual_height * multiply_factor
            name = "Custom Size"
        else:
            # Extract resolution name and dimensions using the key
            selected_info = self.size_dict[size_selected]
            width = selected_info["width"] * multiply_factor
            height = selected_info["height"] * multiply_factor
            name = selected_info["name"]
        
        return (width, height, name)
=======
    def return_res(self, size_selected, multiply_factor):
        # Extract resolution name and dimensions using the key
        selected_info = self.size_dict[size_selected]
        width = int(selected_info["width"] * multiply_factor)
        height = int(selected_info["height"] * multiply_factor)
        name = selected_info["name"]
        return (width, height,name)
>>>>>>> upstream/main

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
