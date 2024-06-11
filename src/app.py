import os
import json 

from services.SqlRawReaderService import SqlRawReaderService
from services.FileHelper import FileHelper

############
config_file = f"config.yaml"
############

def wrt(msg):
    print(msg)

############

wrt("SqlBadger started.")
config = FileHelper.read_config(config_file)
wrt(f"Configs are read : {json.dumps(config.__dict__) }")

file_service = SqlRawReaderService(config)

raw_sql_data = file_service.read_files_recursively()

wrt("SqlBadger finished.")