class BaseTransformerService:
    def __init__(self) -> None:
        pass

    def replacer(self, data_str : str, change_group : dict) -> str:
        tmp = data_str

        for key, val in change_group.items():
            tmp = tmp.replace(f"@{key}", val)

        return tmp
    
    def split_sql(self, sql_str : str) -> list[str]:
        tmp_spltd = sql_str.split(';')
        tmp_spltd = [f"{x};".strip() for x in tmp_spltd if x]
        return tmp_spltd