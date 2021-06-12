def get_cors_headers():
    return {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': True,
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, x-api-key',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
    }


def apply_cache_control_headers(max_age=0):
    if max_age:
        return {
            'Cache-Control': f"public, max-age={max_age}"
        }
    else:
        return {
            'Cache-Control': 'private, max-age=0, no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
        }
