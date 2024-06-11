import os

from services.SqlRawReaderService import SqlRawReaderService
from services.FileHelper import FileHelper

config_file = f"config.yaml"
config = FileHelper.read_config(config_file)

file_service = SqlRawReaderService(config)

raw_sql_data = file_service.read_files_recursively()