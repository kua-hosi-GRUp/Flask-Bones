from flask import request, redirect, url_for, render_template, flash, g
from flask.ext.babel import gettext
from flask.ext.login import login_required

from app.data.models.group import Group
from app.public.forms import EditGroupForm
from . import group


@group.route('/list', methods=['GET', 'POST'])
@login_required
def list():

    from app.data import DataTable
    datatable = DataTable(
        model=Group,
        sortable=[Group.nazev, Group.created_ts],
        searchable=[Group.nazev],
        limits=[25, 50, 100],
        request=request
    )

    if g.pjax:
        return render_template(
            'groups.html',
            datatable=datatable
        )

    return render_template(
        'group-list.html',
        datatable=datatable
    )


@group.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    group = Group.query.filter_by(id=id).first_or_404()
    form = EditGroupForm(obj=group)
    if form.validate_on_submit():
        form.populate_obj(group)
        group.update()
        flash(
            gettext('Group {nazev} edited'.format(nazev=group.nazev)),
            'success'
        )
    return render_template('group-edit.html', form=form, group=group)


@group.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    group = Group.query.filter_by(id=id).first_or_404()
    group.delete()
    flash(
        gettext('Group {nazev} deleted').format(nazev=group.nazev),
        'success'
    )
    return redirect(url_for('.list'))
