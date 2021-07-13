import os

from src.functions.searchby.service import search_by
from src.utils.http.response import make_response

DYNAMODB_ITEMS_TABLE_NAME = os.getenv('DYNAMODB_ITEMS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_ITEMS_TABLE_NAME: {DYNAMODB_ITEMS_TABLE_NAME}')
    print(f'event: {event}')
    try:
        if event['queryStringParameters'] is not None:
            request_query = event['queryStringParameters']
            items = search_by(DYNAMODB_ITEMS_TABLE_NAME, request_query['title'])

        result = {
            "items": items
        }
        return make_response(context.aws_request_id, 0, 200, result)
    except ValueError as error:
        return make_response(context.aws_request_id, 0, 409, None, "CONFLICT_ERROR", str(error))
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))

