from flask_restful import Api
from handlers.auth import AuthLogin, AuthHello, AuthLogout
from handlers.user import UserIndex, UserSingle

class Router:
    @staticmethod
    def init(app):
        api = Api(app)

        # Auth
        api.add_resource(AuthLogin, '/api/login')
        api.add_resource(AuthHello, '/api/hello')
        api.add_resource(AuthLogout, '/api/logout')

        # User
        api.add_resource(UserIndex, '/api/users')
        api.add_resource(UserSingle, '/api/users/<int:id>')

        return api