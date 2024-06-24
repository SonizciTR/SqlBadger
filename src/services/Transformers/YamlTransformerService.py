import yaml

from models.SqlContainer import SqlContainer
from models.SqlModel import SqlModel
from services.FileHelper import FileHelper
from services.Transformers.BaseTransformerService import BaseTransformerService


class YamlTransformerService(BaseTransformerService):
    def __init__(self) -> None:
        pass

    def process(self, model: SqlContainer) -> SqlContainer:
        raw_sql_whole = model.sql_raw_data

        keys_to_replace = model.yaml_data.get("replace")
        if(keys_to_replace is not None):
            raw_sql_whole = self.replacer(raw_sql_whole, keys_to_replace)
        
        spltd_raw_sqls = self.split_sql(raw_sql_whole)

        model.sub_sqls = self.convert_to_sql_model(model, spltd_raw_sqls)

        return model
    
    def convert_to_sql_model(self, model: SqlContainer, raw_sqls : list[str]) -> list[SqlModel]:
        depo_sqls = list[SqlModel]()

        for itm_raw_sql in  raw_sqls:
            sql_model = SqlModel(itm_raw_sql)
            depo_sqls.append(sql_model)
        
        return depo_sqls