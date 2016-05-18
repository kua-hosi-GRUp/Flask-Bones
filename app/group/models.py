from flask.ext.login import UserMixin
from app.extensions import cache, bcrypt
from app.database import db, CRUDMixin
import datetime


class Group(CRUDMixin, UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.String(128), nullable=False, unique=True)
    created_ts = db.Column(db.DateTime(), nullable=False)
    users = db.relationship('User', backref='in_group', lazy='dynamic')
    # TODO: Establish which users are admins

    def __init__(self, nazev):
        self.nazev = nazev

    def __repr__(self):
        return '<Group %s>' % self.nazev
