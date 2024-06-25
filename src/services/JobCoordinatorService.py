import threading
import time

from models.SqlContainer import SqlContainer


class JobCoordinatorService():
    def __init__(self, sql_engine_to_use, sqls_to_run : list[SqlContainer]) -> None:
        self.sql_engine = sql_engine_to_use
        self.sqls_all = sorted(sqls_to_run)
        pass

    def start(self) -> None:
        pass
