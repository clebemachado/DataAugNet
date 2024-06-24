from albumentation import AbstractAlbumentation
from models import LabeledImage

class UnetAlbumentation(AbstractAlbumentation):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def process(self, labeled_image: LabeledImage):
        """
        Processes the albumentation for Unet.
        """
        print("Processing Albumentation for Unet...")
    
    def __repr__(self):
        return f"UnetAlbumentation(args={self.kwargs})"