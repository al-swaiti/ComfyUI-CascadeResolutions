import os
import json
class CascadeResolutions:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        s.size_sizes, s.size_dict = read_sizes()
        return {'required': {'size_selected': (s.size_sizes,)}}

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("x","y")
    FUNCTION = "return_res"
    OUTPUT_NODE = True
    CATEGORY = "Resolution"

    def return_res(self, size_selected):
        width = self.size_dict[size_selected]["width"]
        height = self.size_dict[size_selected]["height"]
        return ({"x":width},{"y": height})
        pass

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "CascadeResolutions": CascadeResolutions
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CascadeResolutions": "Cascade Resolutions"
}
def read_sizes():
    p = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(p, 'sizes.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    size_sizes = list(data['sizes'].keys())
    size_dict = data['sizes']
    return size_sizes, size_dict