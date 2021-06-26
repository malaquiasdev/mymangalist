import json
import os

from src.functions.createnewitem.service import create_new_item_if_not_exist_in_my_list
from src.utils.http.response import make_response

DYNAMODB_ITEMS_TABLE_NAME = os.getenv('DYNAMODB_ITEMS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_ITEMS_TABLE_NAME: {DYNAMODB_ITEMS_TABLE_NAME}')
    print(f'event: {event}')
    request_body = json.loads(event['body'])

    try:
        create_new_item_if_not_exist_in_my_list(DYNAMODB_ITEMS_TABLE_NAME, request_body.get('slug'),
                                                request_body.get(
                                                    'title'), request_body.get('status'),
                                                request_body.get('type'))
    except ValueError as error:
        return make_response(context.aws_request_id, 0, 409, None, "CONFLICT_ERROR", str(error))
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))
    else:
        return make_response(context.aws_request_id, 0, 201, request_body)
