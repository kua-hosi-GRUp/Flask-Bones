from flask_wtf import Form
from flask.ext.babel import gettext, lazy_gettext
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired, Length

from app.data.models import Group


class GroupForm(Form):
    nazev = TextField(lazy_gettext('Group Name'), validators=[DataRequired(lazy_gettext('This field is required.')), Length(min=2, max=128)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class RegisterGroupForm(GroupForm):
    accept_tos = BooleanField(lazy_gettext('I accept the TOS'), validators=[DataRequired(lazy_gettext('This field is required.'))])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        group = Group.query.filter_by(nazev=self.nazev.data).first()
        if group:
            self.nazev.errors.append(gettext('Group name already registered'))
            return False

        self.group = group
        return True


class EditGroupForm(GroupForm):
    pass
