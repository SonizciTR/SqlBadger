
class SqlModel:
    
    COMMANDS = ["THREAD"]
    CMD_LINE_THREAD = f"--{COMMANDS[0]}"

    def __init__(self, raw_sql : str) -> None:
        self.raw_sql = raw_sql
        self.is_parallel = False
        self.parallel_count = 1
        self.sql_ready = []

        self.assign_values(raw_sql)
    
    def assign_values(self, raw_sql : str) -> None:
        if not any(ext in raw_sql for ext in self.COMMANDS):
            self.sql_ready.append(raw_sql)
            return

        self.parallel_count = self.get_parallel_count(raw_sql)
            
        #By request, @Thread starts from 1 and two decimals 
        for itm_thread in range(1, self.parallel_count + 1):
            tmp_val = str(itm_thread).zfill(2)
            tmp_sql = raw_sql.replace(f"@{self.COMMANDS[0]}", tmp_val)

            self.sql_ready.append(tmp_sql)
            pass
        pass

    def get_parallel_count(self, text_raw_sql : str) -> int:
        all_lines = text_raw_sql.splitlines()
        for itm_sub_lines in all_lines: 
            if not (self.CMD_LINE_THREAD  in itm_sub_lines): continue
            tmp_cleaned = itm_sub_lines.replace(' ','')
            tmp_cleaned = tmp_cleaned.replace(f"{self.CMD_LINE_THREAD}:",  "")
            return int(tmp_cleaned)
        
        return 1
