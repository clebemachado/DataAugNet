from abc import ABC, abstractmethod
from pathlib import Path
import shutil

class AbstractSaveFile(ABC):
    def __init__(self, label:str) -> None:
        self.create_folder(label)
        
    def create_folder(self, label:str):
        print("Creating folders to save data....")
        path_content = Path("./content")

        if path_content.exists() and path_content.is_dir():
            shutil.rmtree(path_content)
            
        path_content.mkdir(parents=True, exist_ok=True)

        (path_content / 'train').mkdir(parents=True, exist_ok=True)
        (path_content / 'train/imagens').mkdir(parents=True, exist_ok=True)
        (path_content / f'train/{label}').mkdir(parents=True, exist_ok=True)
        (path_content / 'train/views').mkdir(parents=True, exist_ok=True)

        (path_content / 'test').mkdir(parents=True, exist_ok=True)
        (path_content / 'test/imagens').mkdir(parents=True, exist_ok=True)
        (path_content / f'test/{label}').mkdir(parents=True, exist_ok=True)
        (path_content / 'test/views').mkdir(parents=True, exist_ok=True)

        (path_content / 'validation').mkdir(parents=True, exist_ok=True)
        (path_content / 'validation/imagens').mkdir(parents=True, exist_ok=True)
        (path_content / f'validation/{label}').mkdir(parents=True, exist_ok=True)
        (path_content / 'validation/views').mkdir(parents=True, exist_ok=True)
        print("Process completed....")
        