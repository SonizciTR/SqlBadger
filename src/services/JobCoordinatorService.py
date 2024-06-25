import threading
import time
from concurrent.futures import ThreadPoolExecutor

from models.SqlContainer import SqlContainer
from models.SqlModel import SqlModel
from services.LogService import wrt_screen


class JobCoordinatorService():
    def __init__(self, sql_engine_to_use, sqls_to_run : list[SqlContainer]) -> None:
        self.sql_engine = sql_engine_to_use
        self.sqls_all = sorted(sqls_to_run)
        pass

    def start(self) -> int:
        success_count = 0
        for itm_container in self.sqls_all:
            tm_start = time.time()
            tmp_is_success = self.run_sql_package(itm_container)
            tm_end = time.time()

            print(f"[{itm_container.file_name}] job is done(minutes) : {(tm_end- tm_start) / 60.0}")

            if(tmp_is_success): success_count += 1
        
        return success_count
    
    def run_sql_package(self, sql_container : SqlContainer) -> bool:
        all_success = True
        for itm_sql_package in sql_container.sub_sqls:
            if(itm_sql_package.is_parallel):
                tmp_thread_result = []

                with ThreadPoolExecutor(max_workers=itm_sql_package.parallel_count) as exe:
                    tmp_thread_result = exe.map(self.run_query_with_engine, itm_sql_package.sql_ready)
                
                for indx, itm_result in enumerate(tmp_thread_result):
                    all_success &= itm_result.is_success
                    wrt_screen(f"[{sql_container.file_name}][{indx}] numbered thread is_success = {itm_result.is_success}.  message = {itm_result.message}")

                continue

            for itm_sql in itm_sql_package.sql_ready:
                tmp_rslt = self.run_query_with_engine(itm_sql)
                all_success &= tmp_rslt.is_success

        return all_success
    
    def run_query_with_engine(self, query_to_execute : str) -> int:
        return self.sql_engine.run_query(query_to_execute)


