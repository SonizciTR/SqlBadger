
from models.ConfigModel import ConfigModel
from models.SqlContainer import SqlContainer
from services.Transformers.BaseTransformerService import BaseTransformerService
from services.Transformers.YamlTransformerService import YamlTransformerService


class SqlTransformerService(BaseTransformerService):
    def __init__(self, config : ConfigModel = None) -> None:
        self.config = config
        self.yamller = YamlTransformerService()
        pass

    def reshape_sql(self, raw_sql_data : list[SqlContainer]) -> list[SqlContainer]:
        sql_new_list = list[SqlContainer]()
        for itm in raw_sql_data:
            itm = self.yamller.process(itm)
            
            if(itm.suspend): continue

            sql_new_list.append(itm)
        
        return sql_new_list