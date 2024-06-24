from process import AbstractProcessData
from albumentation import YoloAlbumentation
from models import LabeledImage
from save_file import YoloSaveFile
from utils import YOLO_ALBUMENTATION_ERROR_MESSAGE

class YoloProcessData(AbstractProcessData):
    
    def __init__(self, labeled_image: LabeledImage, **kwargs):
        super().__init__(labeled_image, YoloSaveFile(), **kwargs)
    
    def process(self):
        """
        Processes the data for Yolo.
        """
        print("Processing Yolo Process Data...")
        
        self.albumentation_process(YoloAlbumentation, YOLO_ALBUMENTATION_ERROR_MESSAGE)
        
    def __repr__(self):
        return "YoloProcessData()"