class BaseTransformerService:
    def __init__(self) -> None:
        pass

    def replacer(self, data_str : str, change_group : dict) -> str:
        tmp = data_str

        for key, val in change_group.items():
            tmp = tmp.replace(f"@{key}", val)

        return tmp