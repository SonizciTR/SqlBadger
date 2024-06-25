class QueryResult():
    def __init__(self, is_succ : bool, msg : str, affected_row_count : int) -> None:
        self.is_success = is_succ
        self.message = msg
        self.affected_count = affected_row_count
        pass