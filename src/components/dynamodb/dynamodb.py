import typing
import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def create_new_manga(table_name: str, slug: str, title: str, status: str, manga_status: str,
                     num_chapters_read: int, average_score: float, scores: object, external_links: object) -> bool:
    table = dynamodb.Table(table_name)
    table.put_item(Item={
        "slug": slug,
        'title': title,
        'status': status,
        'manga_status': manga_status,
        'num_chapters_read': num_chapters_read,
       # 'average_score': average_score, //TODO THIS MUST BE CALCULATED AND SAVED BASED IN THE SCORE VALUES
        'scores': scores,
        'external_links': external_links
    })
    return True


def find_manga_by_slug(table_name: str, slug: str) -> any:
    table = dynamodb.Table(table_name)
    try:
        response = table.query(KeyConditionExpression=Key('slug').eq(slug))
    except ClientError as error:
        print(error)
        raise
    else:
        return response['Items']


def find_reading_mangas(table_name: str) -> typing.List[any]:
    table = dynamodb.Table(table_name)
    try:
        response = table.scan(FilterExpression=Attr('status').contains("reading"))
    except ClientError as error:
        print(error)
        raise
    else:
        return response['Items']
