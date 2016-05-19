from flask_wtf import Form
from flask.ext.babel import gettext
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired, Length

from app.data.models import Group


class GroupForm(Group):
    nazev = TextField(
        gettext('Name'), validators=[DataRequired(), Length(min=2, max=128)]
    )

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)


class RegisterGroupForm(GroupForm):
    accept_tos = BooleanField(
        gettext('I accept the TOS'), validators=[DataRequired()]
    )

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.nazev = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        nazev = Group.query.filter_by(nazev=self.nazev.data).first()
        if nazev:
            self.nazev.errors.append(gettext('Name already registered'))
            return False

        self.nazev = nazev
        return True


class EditGroupForm(GroupForm):
    pass
