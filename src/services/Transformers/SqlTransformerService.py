
from models.ConfigModel import ConfigModel
from models.SqlModel import SqlModel
from services.Transformers.BaseTransformerService import BaseTransformerService
from services.Transformers.YamlTransformerService import YamlTransformerService


class SqlTransformerService(BaseTransformerService):
    def __init__(self, config : ConfigModel = None) -> None:
        self.config = config
        self.yamller = YamlTransformerService()
        pass

    def reshape_sql(self, raw_sql_data : list[SqlModel]) -> list[SqlModel]:
        sql_new_list = list[SqlModel]
        for itm in raw_sql_data:
            if(itm.is_pure_sql):
                itm.sub_sqls = self.split_sql(itm.raw_data)
            else:
                itm = self.yamller.process(itm)
            
            if(itm.suspend): continue

            sql_new_list.append(itm)
        
        return sql_new_list