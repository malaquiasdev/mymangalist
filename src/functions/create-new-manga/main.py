import json
import os

from src.components.dynamodb import dynamodb

DYNAMODB_MANGAS_TABLE_NAME = os.getenv('DYNAMODB_MANGAS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_MANGAS_TABLE_NAME: {DYNAMODB_MANGAS_TABLE_NAME}')
    print(f'event: {event}')
    request_body = {**event["body"]}
    exist_in_my_list = dynamodb.find_manga_by_slug(DYNAMODB_MANGAS_TABLE_NAME, request_body.get('title'))
    if not exist_in_my_list:
        dynamodb.create_new_manga(DYNAMODB_MANGAS_TABLE_NAME, request_body.get('slug'), request_body.get('title'),
                                  request_body.get('status'), request_body.get('mangaStatus'),
                                  request_body.get('numChaptersRead'), request_body.get('averageScore'),
                                  request_body.get('scores'), request_body.get('externalLinks'))
    result = {
        'data': {
            'contents': '',
        },
        'requestId': context.aws_request_id
    }
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
