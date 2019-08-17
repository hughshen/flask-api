from flask import jsonify
from helpers.error import code_to_msg

def res_json(data = None, msg = None, code = None, total = None):
    if data is None:
        data = []

    if code is None:
        code = '000000'
    elif code_to_msg(code) is None:
        code = '000001'

    if msg is None:
        msg = code_to_msg(code)

    if msg is None:
        msg = ''

    if total is None:
        total = len(data) if type(data) == list else 1

    return jsonify({
        'errMsg': msg,
        'errCode': code,
        'data': data,
        'total': total,
    })

def is_blank(s):
    return not (s and s.strip())