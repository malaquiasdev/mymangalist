from src.utils.http.response import make_response


def handler(event, context):
    print(f'event: {event}')

    result = {
        "hello": "world"
    }
    return make_response(context.aws_request_id, 0, 200, result)
