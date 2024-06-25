import os
import json

from dotenv import load_dotenv
from math import ceil

from services.DremioService import DremioService
from services.LogService import wrt_screen
from services.SqlContainerReaderService import SqlContainerReaderService
from services.FileHelper import FileHelper
from services.JobCoordinatorService import JobCoordinatorService
from services.Transformers.SqlTransformerService import SqlTransformerService

############
load_dotenv()

config_file = f"config.yaml"
############



def mask_string(s, perc=0.6):
    mask_chars = ceil(len(s) * perc)
    return f'{"*" * mask_chars}{s[mask_chars:]}'

def print_all_env():
    wrt_screen("*********** All Environments:")
    
    for key, value in os.environ.items():
        wrt_screen(f'{key}: {mask_string(value)}')
    
    wrt_screen("*****************************")
    

############


############
wrt_screen("SqlBadger started.")
print_all_env()

config = FileHelper.read_config(config_file)
wrt_screen(f"Configs are read : {json.dumps(config.__dict__) }")

file_service = SqlContainerReaderService(config)

raw_sql_data = file_service.read_files_recursively()
wrt_screen(f"Total Raw Sql Query count : {len(raw_sql_data)}")

sql_shaper = SqlTransformerService(config)
sql_ready = sql_shaper.reshape_sql(raw_sql_data)
wrt_screen(f"Total Ready Sql Query count : {len(sql_ready)}")

wrt_screen("Begining to run sqls.")
query_engine = DremioService()
job_runner = JobCoordinatorService(query_engine, sql_ready)
succ_count = job_runner.start()
wrt_screen(f"All jobs runned. Success : {succ_count} / {len(sql_ready)}.")
wrt_screen("All sqls runned.")

############
wrt_screen("SqlBadger finished.")