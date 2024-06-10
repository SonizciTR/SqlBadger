from services.BaseService import BaseService


class ConfigModel(BaseService):
    def __init__(self, raw_data : dict = None) -> None:
        if(raw_data is None): pass
        
        self.folder_source = self.safe_read(raw_data, "folder_source")

        pass