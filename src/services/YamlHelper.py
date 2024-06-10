import yaml

from models.ConfigModel import ConfigModel


class YamlHelper:
    def __init__(self) -> None:
        pass

    def read_yaml(self, yaml_file : str) -> dict:
        yaml_readed = None
        with open(yaml_file, 'r') as file:
            yaml_readed = yaml.safe_load(file)
        return yaml_readed

    def read_config(self) -> ConfigModel:
        tmp_yaml = self.read_yaml("config.yaml")
        return ConfigModel(tmp_yaml)