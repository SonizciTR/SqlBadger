import os

from models.ConfigModel import ConfigModel
from models.SqlModel import SqlModel

class SqlRawReaderService:
    def __init__(self, cnfgModel : ConfigModel) -> None:
        self.config = cnfgModel
        pass
    
    def read_files_recursively(self) -> list[SqlModel]:
        all_sqls = list[SqlModel]

        tmp_dir = f"/{self.config.folder_source}"
        
        for root, dirs, files in os.walk(tmp_dir):
            for file in files:
                tmp_fullpath = os.path.join(root, file)
                if file.endswith(SqlModel.possible_ext):
                    all_sqls.append(SqlModel(tmp_fullpath))
        
        return all_sqls