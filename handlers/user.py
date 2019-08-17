import time
import hashlib
from flask import request, current_app as app
from flask_restful import Resource
from helpers.helper import res_json, is_blank
from models.user import User

class UserIndex(Resource):
    def get(self):
        page = request.args.get('page')
        page = int(page) if page.isdigit() else 1
        page = page if page > 0 else 1

        pager = User.query.order_by(User.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
        data = [user.res_format(password=False, api_token=False) for user in pager.items]
        return res_json(data=data, total=pager.total)

    def post(self):
        u = User()
        u.username = request.form.get('username')
        u.password = request.form.get('password')
        u.created_at = int(time.time())
        u.updated_at = int(time.time())

        if not u.check_before_commit():
            return res_json(code='000301')

        # Check username if exists
        tmp = User.get_single_by_args(username=u.username)
        if tmp is not None:
            return res_json(code='000205')

        try:
            u.password = hashlib.md5(u.password.encode('utf-8')).hexdigest()
            u.create_user_to_db()
            return res_json()
        except Exception as e:
            app.logger.error(e)
        finally:
            pass

        return res_json(code='000202')

class UserSingle(Resource):
    def get(self, id):
        user = User.get_single_by_args(id=id)

        if user is None:
            return res_json(code='000201')

        return res_json(data=user.res_format(password=False, api_token=False))

    def put(self, id):
        u = User.get_single_by_args(id=id)

        if u is None:
            return res_json(code='000201')

        new_username = request.form.get('username')
        new_password = request.form.get('password')

        if is_blank(new_username):
            return res_json(code='000301')

        # Check username if exists
        if u.check_username_exists(new_username) is not None:
            return res_json(code='000205')

        try:
            u.username = new_username
            if not is_blank(new_password):
                u.password = hashlib.md5(new_password.encode('utf-8')).hexdigest()
            u.update_user_to_db()
            return res_json()
        except Exception as e:
            app.logger.error(e)
        finally:
            pass

        return res_json(code='000203')

    def delete(self, id):
        u = User.get_single_by_args(id=id)

        if u is None:
            return res_json(code='000201')

        try:
            u.delete_user_to_db()
            return res_json()
        except Exception as e:
            app.logger.error(e)
        finally:
            pass

        return res_json(code='000204')
