import os

from models.SqlModel import SqlModel
from services.FileHelper import FileHelper

class SqlContainer:
    EXTENSIONS = (".yaml", ".yml")

    def __init__(self, full_file_path : str = None) -> None:
        self.set_default_values()

        if(full_file_path is not None): 
            tmp_full = os.path.realpath(full_file_path)
            self.set(tmp_full)

        pass

    def set_default_values(self):
        self.file_full_path = ""
        self.file_name = ""
        self.extension = ""
        self.raw_yaml = ""

        self.yaml_data = {}
        self.sql_raw_data = ""
        
        self.priority = 99
        self.suspend = False
        self.sub_sqls = list[SqlModel]

        pass

    def set(self, yaml_full_path : str) -> None:
        yaml_filename, yaml_file_extension = os.path.splitext(yaml_full_path)
        yaml_filename = os.path.basename(yaml_full_path)

        self.file_full_path = yaml_full_path
        self.file_name = yaml_filename
        self.extension = yaml_file_extension

        self.raw_yaml = FileHelper.read_file(yaml_full_path)
        self.yaml_data = FileHelper.read_yaml_file(yaml_full_path)

        tmp_base_dir = os.path.dirname(yaml_full_path)
        tmp_sql_rel_path = self.yaml_data.get("sql_file")
        full_sql_file = os.path.join(tmp_base_dir, tmp_sql_rel_path)
        self.sql_raw_data = FileHelper.read_file(full_sql_file)

        pass

    def sanity_check(self, yaml_filename : str, yaml_bag : dict) -> None:
        if(yaml_bag is None):
            raise Exception(f"[{yaml_filename}] files could not readed.")
        tmp_sql_path = yaml_bag.get("sql_file")
        if(tmp_sql_path is None) or (len(tmp_sql_path) == 0):
            raise Exception(f"[{yaml_filename}] file's 'sql_file' property is missing.")
        pass
