import typing
import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def create_new_item(table_name: str, uuid: str, title: str, status: str, type: str) -> bool:
    table = dynamodb.Table(table_name)
    table.put_item(Item={
        'uuid': uuid,
        'title': title,
        'status': status,
        'type': type,
        'scores': []
    })
    return True


def find_item_by_uuid(table_name: str, uuid: str) -> any:
    table = dynamodb.Table(table_name)
    try:
        response = table.query(KeyConditionExpression=Key('uuid').eq(uuid))
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


def find_items_by_title_and_type(table_name: str, title: str, type: str) -> typing.List[any]:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr(
            'title').eq(title) &
                                               Attr('type').contains(type))
    except ClientError as error:
        print(error)
        raise
    else:
        return response['Items']


def find_items_by_title(table_name: str, title: str) -> typing.List[any]:
    table = dynamodb.Table(table_name)
    try:
        print(f'title: {title}')
        response = table.scan(FilterExpression=Attr('title').contains(title))
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
