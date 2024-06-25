import threading
import time
from concurrent.futures import ThreadPoolExecutor

from models.SqlContainer import SqlContainer
from models.SqlModel import SqlModel


class JobCoordinatorService():
    def __init__(self, sql_engine_to_use, sqls_to_run : list[SqlContainer]) -> None:
        self.sql_engine = sql_engine_to_use
        self.sqls_all = sorted(sqls_to_run)
        pass

    def start(self) -> int:
        success_count = 0
        for itm_container in self.sqls_all:
            tmp_is_success = self.run_sql_package(itm_container.sub_sqls)
            
            if(tmp_is_success): success_count += 1
        
        return success_count
    
    def run_sql_package(self, sql_model_list : list[SqlModel]) -> bool:
        for itm_sql_package in sql_model_list:
            if(itm_sql_package.is_parallel):
                tmp_thread_result = []

                with ThreadPoolExecutor(max_workers=itm_sql_package.parallel_count) as exe:
                    tmp_thread_result = exe.map(self.run_query_with_engine, itm_sql_package.sql_ready)
                
                for r in tmp_thread_result:
                    print(f"**** tmp_thread_result = {r.is_success} - {r.message}")

                continue

            for itm_sql in itm_sql_package.sql_ready:
                self.run_query_with_engine(itm_sql)

        return True
    
    def run_query_with_engine(self, query_to_execute : str) -> int:
        return self.sql_engine.run_query(query_to_execute)


