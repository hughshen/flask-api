import hashlib
from flask import request, g
from flask_restful import Resource
from helpers.helper import res_json
from models.user import User

class AuthLogin(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return res_json(code='000103')

        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        user = User.get_single_by_args(username=username, password=password)
        if user is None:
            return res_json(code='000104')

        data = user.res_format(password=False)

        # Update token
        token = user.regenerate_token()

        data['api_token'] = token

        return res_json(data=data)

class AuthHello(Resource):
    def get(self):
        data = 'hello, %s' % g.user.username
        return res_json(data=data)

class AuthLogout(Resource):
    def put(self):
        g.user.clear_user_token()
        return res_json()