
from models.ConfigModel import ConfigModel
from models.SqlModel import SqlModel
from services.Transformers.BaseTransformerService import BaseTransformerService


class SqlTransformerService(BaseTransformerService):
    def __init__(self, config : ConfigModel = None) -> None:
        self.config = config
        pass

    def reshape_sql(raw_sql_data : list[SqlModel]) -> list[SqlModel]:
        for itm in raw_sql_data:
            pass
        pass