import os

from models.ConfigModel import ConfigModel

class FileService:
    def __init__(self, cnfgModel : ConfigModel) -> None:
        self.config = cnfgModel
        pass

    def read_files(self) -> list:
        pass