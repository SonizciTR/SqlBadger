import os

from services.FileHelper import FileHelper

class SqlModel:
    def __init__(self, full_file_path : str = None) -> None:
        self.possible_ext = (".txt", ".yaml", ".yml")

        self.file_full_path = ""
        self.file_name = ""
        self.extension = ""
        self.raw_data = ""

        if(full_file_path is not None): self.set(full_file_path)

        pass

    def set(self, fullPath : str) -> None:
        filename, file_extension = os.path.splitext(fullPath)

        self.file_full_path = fullPath
        self.file_name = filename
        self.extension = file_extension
        self.raw_data = FileHelper.read_file(fullPath)

        pass
