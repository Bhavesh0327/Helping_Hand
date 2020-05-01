def error_response(msg):
    return {
        'status_code': 400,
        'data': msg
    }