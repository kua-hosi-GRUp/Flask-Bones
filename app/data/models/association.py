from ..mixins import CRUDMixin
from .. import db

class Association(CRUDMixin, db.Model):
    __tablename__ = 'association'
    left_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    right_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    #extra_data = db.Column(db.String(50))
    users = db.relationship("User", back_populates="groups")
    groups = db.relationship("Group", back_populates="users")