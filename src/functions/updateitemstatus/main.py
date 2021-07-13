import json
import os

from src.functions.updateitemstatus.service import update_item_status
from src.utils.http.response import make_response

DYNAMODB_ITEMS_TABLE_NAME = os.getenv('DYNAMODB_ITEMS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_ITEMS_TABLE_NAME: {DYNAMODB_ITEMS_TABLE_NAME}')
    print(f'event: {event}')
    try:
        request_path = event['pathParameters']
        request_body = json.loads(event['body'])
        updated = update_item_status(DYNAMODB_ITEMS_TABLE_NAME, request_path['uuid'], request_body.get('status'))
        result = {
            "uuid": request_path['uuid'],
            "updated": updated
        }
        return make_response(context.aws_request_id, 0, 200, result)
    except ValueError as error:
        return make_response(context.aws_request_id, 0, 409, None, "CONFLICT_ERROR", str(error))
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))

