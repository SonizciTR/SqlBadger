import pyarrow

from services.FileService import FileService
from services.YamlHelper import YamlHelper

config = YamlHelper.read_config()

file_service = FileService(config)

raw_sql_data = file_service.read_files()