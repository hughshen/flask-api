import secrets
from models import db, BaseModel
from helpers.helper import is_blank

class User(db.Model, BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    api_token = db.Column(db.String(255), nullable=False, default='')
    created_at = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.Integer, nullable=False)

    def regenerate_token(self):
        token = secrets.token_hex(16).upper()
        self.api_token = token
        db.session.commit()

        return token

    def clear_user_token(self):
        self.api_token = ''
        db.session.commit()

    def create_user_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_user_to_db(self):
        db.session.commit()

    def delete_user_to_db(self):
        db.session.delete(self)
        db.session.commit()

    def check_before_commit(self):
        if is_blank(self.username) or is_blank(self.password):
            return False
        return True

    def check_username_exists(self, username):
        return User.query.filter(User.username == username, User.id != self.id).first()

    @staticmethod
    def get_single_by_args(**kwargs):
        return User.query.filter_by(**kwargs).first()
