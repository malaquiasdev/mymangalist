import typing
import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def create_new_item(table_name: str, slug: str, title: str, status: str, type: str) -> bool:
    table = dynamodb.Table(table_name)
    table.put_item(Item={
        'slug': slug,
        'title': title,
        'status': status,
        'type': type,
        'scores': []
    })
    return True


def find_item_by_slug(table_name: str, slug: str) -> any:
    table = dynamodb.Table(table_name)
    try:
        response = table.query(KeyConditionExpression=Key('slug').eq(slug))
    except ClientError as error:
        print(error)
        raise
    else:
        if response['Count'] > 0:
            return response['Items'][0]
        else:
            return None


def find_items_by_status_and_type(table_name: str, status: str, type: str) -> typing.List[any]:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(
            'status').contains(status) &
            Attr('type').contains(type))
    except ClientError as error:
        print(error)
        raise
    else:
        return response['Items']


def find_all_items(table_name: str) -> any:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
    except ClientError as error:
        print(error)
        raise
    finally:
        return data


def update_item(table_name: str, item: dict) -> bool:
    table = dynamodb.Table(table_name)
    table.put_item(Item={
        **item
    })
    return True
