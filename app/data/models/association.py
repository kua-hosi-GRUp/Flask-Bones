from ..mixins import CRUDMixin
from .. import db

class Association(CRUDMixin, db.Model):
    __tablename__ = 'association'
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    users = db.relationship("User", back_populates="groups")
    groups = db.relationship("Group", back_populates="users")