class BaseService:
    def __init__(self) -> None:
        pass

    def safe_read(self, data : dict, key_word : str) :
        return data.get(key_word)

    def safe_read_dict(self, data : dict, keys : list) :
        if(data is None) : return None

        tmp_data = self.safe_read(data, keys[0])

        if(len(keys) == 1): return tmp_data

        return self.safe_read_dict(tmp_data, keys[1:])
