import os

from services.FileHelper import FileHelper

class SqlModel:
    EXTENSIONS = (".sql", ".yaml", ".yml")

    def __init__(self, full_file_path : str = None) -> None:
        self.set_default_values()

        filename, file_extension = os.path.splitext(full_file_path)

        if(full_file_path is not None): self.set(full_file_path, filename, file_extension.lower())

        pass

    def set_default_values(self):
        self.file_full_path = ""
        self.file_name = ""
        self.extension = ""
        self.raw_data = ""
        self.is_pure_sql = False

        self.sql_ready = ""
        self.priority = 99
        self.suspend = False

        pass

    def set(self, fullPath : str, filename : str, file_extension : str) -> None:
        if(file_extension == ".sql"): self.is_pure_sql = True

        self.file_full_path = fullPath
        self.file_name = filename
        self.extension = file_extension
        self.raw_data = FileHelper.read_file(fullPath)

        pass
