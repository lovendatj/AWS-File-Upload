from pathlib import Path

from .FileData import read_json

config_path = Path(__file__).parent / "service_alias.json"
config_data = read_json(config_path)


def bucket_lookup(bucket_alias: str = None) -> str:
    return config_data['aws-services']['s3'][bucket_alias]


def table_lookup(table_alias: str = None) -> str:
    return config_data['aws-services']['dynamo'][table_alias]
