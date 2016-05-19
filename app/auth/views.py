from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask.ext.babel import gettext
from flask.ext.login import login_user, login_required, logout_user
from app.extensions import lm
from app.data.models import User
from app.auth import auth


@lm.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash(gettext('You were logged out'), 'success')
    return redirect(url_for('public.login'))