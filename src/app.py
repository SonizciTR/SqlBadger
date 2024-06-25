import os
import json
from datetime import datetime 
from dotenv import load_dotenv
from math import ceil

from services.DremioService import DremioService
from services.SqlContainerReaderService import SqlContainerReaderService
from services.FileHelper import FileHelper
from services.JobCoordinatorService import JobCoordinatorService
from services.Transformers.SqlTransformerService import SqlTransformerService

############
load_dotenv()

config_file = f"config.yaml"
############

def wrt(msg):
    date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    print(f"[{date_time}] => {msg}")

def mask_string(s, perc=0.6):
    mask_chars = ceil(len(s) * perc)
    return f'{"*" * mask_chars}{s[mask_chars:]}'

def print_all_env():
    wrt("*********** All Environments:")
    
    for key, value in os.environ.items():
        wrt(f'{key}: {mask_string(value)}')
    
    wrt("*****************************")
    

############


############
wrt("SqlBadger started.")
print_all_env()

config = FileHelper.read_config(config_file)
wrt(f"Configs are read : {json.dumps(config.__dict__) }")

file_service = SqlContainerReaderService(config)

raw_sql_data = file_service.read_files_recursively()
wrt(f"Total Raw Sql Query count : {len(raw_sql_data)}")

sql_shaper = SqlTransformerService(config)
sql_ready = sql_shaper.reshape_sql(raw_sql_data)
wrt(f"Total Ready Sql Query count : {len(sql_ready)}")

wrt("Begining to run sqls.")
query_engine = DremioService()
job_runner = JobCoordinatorService(query_engine, sql_ready)
job_runner.start()
wrt("All sqls runned.")

############
wrt("SqlBadger finished.")