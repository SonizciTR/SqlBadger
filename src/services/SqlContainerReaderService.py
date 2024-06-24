import os

from models.ConfigModel import ConfigModel
from models.SqlContainer import SqlContainer

class SqlContainerReaderService:
    def __init__(self, cnfgModel : ConfigModel) -> None:
        self.config = cnfgModel
        pass
    
    def read_files_recursively(self) -> list[SqlContainer]:
        all_sqls = list[SqlContainer]()

        tmp_dir = f"{self.config.folder_source}"
        
        for root, dirs, files in os.walk(tmp_dir):
            for file in files:
                tmp_fullpath = os.path.join(root, file)
                if file.endswith(SqlContainer.EXTENSIONS):
                    tmp_model = SqlContainer(tmp_fullpath)
                    all_sqls.append(tmp_model)
        
        return all_sqls