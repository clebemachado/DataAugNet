
from models.labeled_image import LabeledImage
from process import AbstractProcessData
from albumentation import UnetAlbumentation
from save_file import UnetSaveFile
from utils import UNET_ALBUMENTATION_ERROR_MESSAGE

class UnetProcessData(AbstractProcessData):
    
    def __init__(self, labeled_image: LabeledImage, **kwargs):
        super().__init__(labeled_image, UnetSaveFile(), **kwargs)
    
    def process(self):
        """
        Processa os dados para Unet.
        """
        print("Processing Unet Process Data...")
        
        self.albumentation_process(UnetAlbumentation, UNET_ALBUMENTATION_ERROR_MESSAGE)


    def __repr__(self):
        return "UnetProcessData()"