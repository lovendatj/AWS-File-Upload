from ..Utils.Configuration import bucket_lookup
from typing import Any
import boto3
S3 = boto3.client('s3')


def upload_file(file: str, bucket_alias: str) -> tuple:
    bucket_name = bucket_lookup(bucket_alias)['name']
    fname = file.name.replace('\\', '/').split('/')[-1]

    print(f'[WRITING] {fname} --> {bucket_name}.')
    try:
        S3.upload_fileobj(file, bucket_name, fname)
        return fname, f'https://{bucket_name}.s3.amazonaws.com/{fname}'.replace(' ', '+')
    except Exception as error:
        print(error)
        return False, error
