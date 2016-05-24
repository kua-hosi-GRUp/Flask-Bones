from flask_wtf import Form
from flask.ext.babel import gettext, lazy_gettext
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired, Length

from app.data.models import Group


class GroupForm(Form):
    nazev = TextField(lazy_gettext('Group Name'), validators=[DataRequired(), Length(min=2, max=128)])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class RegisterGroupForm(GroupForm):
    nazev = TextField(lazy_gettext('Group Name'), validators=[DataRequired(lazy_gettext('This field is required.')), Length(min=2, max=128)])
    accept_tos = BooleanField(lazy_gettext('I accept the TOS'), validators=[DataRequired(lazy_gettext('This field is required.'))])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)



class EditGroupForm(GroupForm):
    pass
