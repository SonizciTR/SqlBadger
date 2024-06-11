import os
import json 

from services.SqlRawReaderService import SqlRawReaderService
from services.FileHelper import FileHelper
from services.Transformers.SqlTransformerService import SqlTransformerService

############
config_file = f"config.yaml"
############

def wrt(msg):
    print(msg)

############

wrt("SqlBadger started.")
############

config = FileHelper.read_config(config_file)
wrt(f"Configs are read : {json.dumps(config.__dict__) }")

file_service = SqlRawReaderService(config)

raw_sql_data = file_service.read_files_recursively()
wrt(f"Total Raw Sql Query count : {len(raw_sql_data)}")

sql_shaper = SqlTransformerService(config)
sql_ready = sql_shaper.reshape_sql(raw_sql_data)
wrt(f"Total Ready Sql Query count : {len(sql_ready)}")


############
wrt("SqlBadger finished.")