from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask.ext.babel import gettext
from flask.ext.login import login_user, login_required, logout_user
from itsdangerous import URLSafeSerializer, BadSignature
from app.public.forms import RegisterGroupForm
from app.extensions import lm
from app.data.models import User, Group
from . import auth


@lm.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash(gettext('You were logged out'), 'success')
    return redirect(url_for('public.login'))


@auth.route('/create_group', methods=['GET', 'POST'])
@login_required
def create_group():
    form = RegisterGroupForm()
    if form.validate_on_submit():

        group = Group.create(
            nazev=form.data['nazev'],
        )

        flash(
            gettext(
                'Group {name} created'.format(
                    name=group.nazev
                )
            ),
            'success'
        )
        return redirect(url_for('public.index'))
    return render_template('create_group.html', form=form)

@auth.route('/group/add/<int:id>', methods=['GET', 'POST'])
def group_add_user(id):
    group = Group.query.filter_by(id=id).first_or_404()
    users = User.query.all()
    return render_template('group_add_users.html', users=users)