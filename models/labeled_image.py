import json
import numpy as np
from pathlib import WindowsPath

class LabeledImage:
    def __init__(self, path:WindowsPath):
        
        """
        :param path: caminho do arquivo json com as marcações.
        """
        
        self.path = path
        self.shapes = None
        self.image_path = None
        self.file_name = None
        self.image_height = None
        self.image_width = None
        self.__load_data()

    def __repr__(self):
        return f"LabeledImage(image_path={self.image_path}, image_height={self.image_height}, image_width={self.image_width})"
    
    def __load_data(self):
        """
        Do not keep read base64 or image arrays to optimize memory!
        """
        
        json_file = None
        
        with open(self.path) as file:
            json_file = json.load(file)
            
            necessary_keys = {'imagePath', 'imageHeight', 'imageWidth', 'shapes'}
            json_file = {key: value for key, value in json_file.items() if key in necessary_keys}

            for shape in json_file['shapes']:
                shape_keys = {'label', 'points', 'shape_type'}
                shape = {key: value for key, value in shape.items() if key in shape_keys}
                shape['points'] = np.array(shape['points'])
        
        self.shapes = json_file["shapes"]
        self.file_name = json_file["imagePath"].replace(".jpg", "").replace("png", "")
        self.image_height = json_file["imageHeight"]
        self.image_width = json_file["imageWidth"]
        self.image_path = str((self.path.parent / json_file["imagePath"]).resolve()) # OpenCv doesn't read PathLib 
        
    
    @property
    def create_black_image(self):
        return np.zeros((self.image_height, self.image_width, 1), dtype=np.uint8) # Switch to one channel only