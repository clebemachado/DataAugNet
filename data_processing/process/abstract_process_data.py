from abc import ABC, abstractmethod
from models import LabeledImage
from data_processing.albumentation import AbstractAlbumentation
from save_file import AbstractSaveFile

class AbstractProcessData(ABC):
    def __init__(self, labeled_image: LabeledImage, save_file:AbstractSaveFile, **kwargs):
        """
        Abstract class for data processing.

        :param labeled_image: LabeledImage instance.
        :param kwargs: Additional arguments.
        """
        self.labeled_image = labeled_image
        self.save_file = save_file
        self.kwargs = kwargs
        
    
    @abstractmethod
    def process(self):
        """
        Abstract method for processing data.

        """
        pass
    
    def has_key(self, key):
        """
        Checks if the key is present in the kwargs.

        :param key: Key to be verified.
        :return: True if the key is present, False otherwise.
        """
        return key in self.kwargs
    
    def albumentation_process(self, class_type, error_message:str):
        if self.has_key("albumentation"):
            albumentation:AbstractAlbumentation = self.kwargs["albumentation"]
            if not isinstance(albumentation, class_type):
                raise ValueError(error_message)
            albumentation.process(self.labeled_image)