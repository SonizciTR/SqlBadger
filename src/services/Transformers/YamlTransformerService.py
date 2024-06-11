from models.SqlModel import SqlModel
from services.Transformers.BaseTransformerService import BaseTransformerService


class YamlTransformerService(BaseTransformerService):
    def __init__(self) -> None:
        pass

    def process(self, model: SqlModel) -> SqlModel:
        return model