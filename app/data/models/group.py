from .. import db
from ..mixins import CRUDMixin
import datetime

class Group(CRUDMixin, db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.String(128), nullable=False, unique=True)
    created_ts = db.Column(db.DateTime(), nullable=False)
    users = db.relationship("U_G_Association", back_populates="groups")
    firmy = db.relationship("G_F_Association", back_populates="groups")
    # TODO: Establish which users are admins

    def __init__(self, nazev):
        self.nazev = nazev
        self.created_ts = datetime.datetime.now()

    def __repr__(self):
        return '<Group %s>' % self.nazev

    @staticmethod
    def if_exists(group):
        if not Group.query.filter_by(nazev=group).first():
            return False
        return True