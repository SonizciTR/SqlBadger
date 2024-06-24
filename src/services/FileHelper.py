import yaml

from models.ConfigModel import ConfigModel


class FileHelper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_file(file_name : str) -> str:
        data = ""
        with open(file_name,"r") as frd:
            data = frd.read().replace('\n', ' ')
            #data = frd.read()
            frd.close()

        return data

    @staticmethod
    def read_yaml_file(yaml_file_path : str) -> dict:
        yaml_readed = None
        with open(yaml_file_path, 'r') as file:
            yaml_readed = yaml.safe_load(file)
        return yaml_readed

    @staticmethod
    def read_config(file_config) -> ConfigModel:
        tmp_yaml = FileHelper.read_yaml_file(file_config)
        return ConfigModel(tmp_yaml)