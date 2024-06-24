from save_file import AbstractSaveFile

class YoloSaveFile(AbstractSaveFile):
    
    def __init__(self) -> None:
        self.label = "labels"
        super().__init__(self.label)
    