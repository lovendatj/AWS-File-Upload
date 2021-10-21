import boto3
import json
from typing import Any
from ..Utils.Configuration import table_lookup
from ..Utils.Identification import get_id

DynamoDB = boto3.resource('dynamodb')


def insert_row(table_alias: str, data: dict) -> str:
    table_dict = table_lookup(table_alias)
    table_name, table_key = table_dict['name'], table_dict['key']
    data[table_key] = get_id()
    DynamoDB.Table(table_name).put_item(Item=data)
    print(f'Added to {table_name} table. ItemID: {data[table_key]}')
    return data[table_key]


def read_row(table_alias: str, id: str) -> dict:
    table_dict = table_lookup(table_alias)
    table_name, table_key = table_dict['name'], table_dict['key']
    results = DynamoDB.Table(table_name).get_item(Key={table_key: id})
    return results


def remove_row(table_alias: str, id: str) -> True:
    table_dict = table_lookup(table_alias)
    table_name, table_key = table_dict['name'], table_dict['key']
    try:
        DynamoDB.Table(table_name).delete_item(Key={table_key: id})
    except Exception as error:
        print(error)
        return False
    return True


def update_row(table_alias: str, id: str, param: str, val: Any) -> None:
    table_dict = table_lookup(table_alias)
    table_name, table_key = table_dict['name'], table_dict['key']
    try:
        DynamoDB.Table(table_name).update_item(
            Key={table_key: id},
            UpdateExpression=f'SET {param} = :val1',
            ExpressionAttributeValues={
                ':val1': val
            }
        )
    except Exception as error:
        print(error)
        return False
    return True
