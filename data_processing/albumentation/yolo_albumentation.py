from albumentation import AbstractAlbumentation
from models import LabeledImage

class YoloAlbumentation(AbstractAlbumentation):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def process(self, labeled_image: LabeledImage):
        """
        Process albumentation for Yolo.
        """
        print("Processing Albumentation for Yolo...")
    
    def __repr__(self):
        return f"YoloAlbumentation(args={self.kwargs})"