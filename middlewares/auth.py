from flask import g
from helpers.helper import res_json
from models.user import User

def api_token_middleware(request):
    path = request.path
    method = request.method

    if not path.startswith('/api/') or (path == '/api/login' and method == 'POST'):
        return None

    token = request.headers.get('Api-Token')
    if token is None:
        return res_json(code='000101')
    else:
        # Check token in db
        user = User.get_single_by_args(api_token=token)
        if user is None:
            return res_json(code='000102')
        else:
            g.user = user
