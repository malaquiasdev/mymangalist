import os

from src.functions.listmyscores.service import list_my_scores
from src.utils.http.response import make_response

DYNAMODB_ITEMS_TABLE_NAME = os.getenv('DYNAMODB_ITEMS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_ITEMS_TABLE_NAME: {DYNAMODB_ITEMS_TABLE_NAME}')
    print(f'event: {event}')
    try:
        request_path = event['pathParameters']
        my_scores = list_my_scores(
            DYNAMODB_ITEMS_TABLE_NAME, request_path['slug'])
        result = {
            "scores": my_scores
        }
        return make_response(context.aws_request_id, 0, 200, result)
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))
