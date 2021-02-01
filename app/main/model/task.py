from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class Task(db.Model):
    """ Task Model for storing task related details """
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Task '{}'>".format(self.title)

    