import threading
import time

from models.SqlContainer import SqlContainer


class SqlRunnerService():
    def __init__(self, sqls_to_run : list[SqlContainer]) -> None:
        self.sqls_all = sorted(sqls_to_run)
        pass

    def start(self) -> None:
        pass
