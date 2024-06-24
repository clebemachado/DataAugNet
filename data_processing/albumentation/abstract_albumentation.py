from abc import ABC, abstractmethod
from models import LabeledImage

class AbstractAlbumentation(ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    @abstractmethod
    def process(self, labeled_image: LabeledImage):
        """
        Abstract method for processing albumenation.

        """
        pass