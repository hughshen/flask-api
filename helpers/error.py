error_code_list = {
    '000001': 'System error',
    '000002': '404 Not Found',
    # auth
    '000101': 'Token is required',
    '000102': 'Invalid token',
    '000103': 'Username or password is required',
    '000104': 'Username or password error',
    # db
    '000201': 'Object not found',
    '000202': 'Object create fail',
    '000203': 'Object update fail',
    '000204': 'Object delete fail',
    '000205': 'Object exists',
    # param
    '000301': 'Params error',
}

def code_to_msg(code):
    return error_code_list.get(code)