import json
from .headers import apply_cache_control_headers, get_cors_headers


def _parse_to_aws_model(status_code: int, headers: object, body: object):
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body)
    }


def _make_success_body(request_id: str, result: object) -> object:
    return {
        'data': {
            **result
        },
        'requestId': request_id
    }


def _make_error_body(request_id: str, error_code: str, error_message: str) -> object:
    print(f"request_id: {request_id} | error_code: {error_code} | error_message: {error_message}")
    return {
        "error": {
            "code": error_code,
            "message": error_message,
        },
        'requestId': request_id
    }


def _make_headers(cache_max_age: int) -> object:
    return {
        **get_cors_headers(),
        **apply_cache_control_headers(cache_max_age)
    }


def make_response(request_id: str, cache_max_age: int, status_code=200, result=None,
                  error_code=None, error_message=None) -> object:
    if result:
        return _parse_to_aws_model(status_code, _make_headers(cache_max_age), _make_success_body(request_id, result))
    else:
        return _parse_to_aws_model(status_code, _make_headers(0), _make_error_body(request_id, error_code, error_message))