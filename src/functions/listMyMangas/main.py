import os

from src.functions.listMyMangas.service import list_my_mangas
from src.utils.http.response import make_response

DYNAMODB_MANGAS_TABLE_NAME = os.getenv('DYNAMODB_MANGAS_TABLE_NAME')


def handler(event, context):
    print(f'DYNAMODB_MANGAS_TABLE_NAME: {DYNAMODB_MANGAS_TABLE_NAME}')
    print(f'event: {event}')
    try:
        if event['queryStringParameters'] is not None:
            request_query = event['queryStringParameters']
            mangas = list_my_mangas(DYNAMODB_MANGAS_TABLE_NAME, request_query['status'])
        else:
            mangas = list_my_mangas(DYNAMODB_MANGAS_TABLE_NAME, None)

        result = {
            "mangas": mangas
        }
        return make_response(context.aws_request_id, 0, 200, result)
    except Exception as error:
        return make_response(context.aws_request_id, 0, 500, None, "INTERNAL_SERVER_ERROR", str(error))
