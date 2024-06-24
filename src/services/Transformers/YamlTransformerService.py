import yaml

from models.SqlModel import SqlModel
from services.FileHelper import FileHelper
from services.Transformers.BaseTransformerService import BaseTransformerService


class YamlTransformerService(BaseTransformerService):
    def __init__(self) -> None:
        pass

    def process(self, model: SqlModel) -> SqlModel:
        #raw_yaml = yaml.safe_load(model.raw_data)
        raw_yaml = FileHelper.read_yaml_file(model.file_full_path)
        tmp_raw_sql = raw_yaml.get("sql")
        model.sub_sqls = self.split_sql(tmp_raw_sql)
        return model