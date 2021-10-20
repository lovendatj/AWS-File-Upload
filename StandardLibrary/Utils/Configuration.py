from pathlib import Path
from typing import Dict

from .FileData import read_json

config_path = Path(__file__).parent / "service_alias.json"
config_data = read_json(config_path)


def notion_baseURL(sub: str = None) -> str:
    if sub is not None:
        return config_data['notion']['baseURL'][sub]
    return config_data['notion']['baseURL']


def bucket_lookup(sub: str = None) -> str:
    pass


def table_lookup(sub: str = None) -> str:
    pass


def lambda_lookup(sub: str = None) -> str:
    pass
