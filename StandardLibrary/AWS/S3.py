import boto3
import os
import json
from typing import Any
from ..Utils.Configuration import bucket_lookup

S3 = boto3.client('s3')


def upload_file(file: str, bucket_alias: str) -> bool:
    bucket_name = bucket_lookup(bucket_alias)['name']
    fname = file.name

    print(f'Writing to {bucket_name}.')
    try:
        S3.upload_fileobj(file, bucket_name, fname)
    except Exception as error:
        print(error)
        return False
    return True
