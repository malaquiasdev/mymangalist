import os
import json

from src.functions.addNewScore.service import add_new_score
from src.utils.http.response import make_response

DYNAMODB_MANGAS_TABLE_NAME = os.getenv('DYNAMODB_MANGAS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_MANGAS_TABLE_NAME: {DYNAMODB_MANGAS_TABLE_NAME}')
    print(f'event: {event}')
    try:
        request_path = event['pathParameters']
        request_body = json.loads(event['body'])
        updated = add_new_score(DYNAMODB_MANGAS_TABLE_NAME, request_path['slug'], request_body['score'])
        result = {
            "slug": request_path['slug'],
            "updated": updated
        }
        return make_response(context.aws_request_id, 0, 200, result)
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))
