from save_file import AbstractSaveFile

class UnetSaveFile(AbstractSaveFile):
    
    def __init__(self) -> None:
        self.label = "masks"
        super().__init__(self.label)
    