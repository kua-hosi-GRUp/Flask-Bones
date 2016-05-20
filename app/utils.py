from flask import flash, request, url_for
from flask.ext.babel import gettext


def flash_errors(form, category='danger'):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                u'%s - %s' % (getattr(form, field).label.text, error),
                category
            )


def url_for_other_page(remove_args=[], **kwargs):
    args = request.args.copy()
    remove_args = ['_pjax']
    for key in remove_args:
        if key in args.keys():
            args.pop(key)
    new_args = [x for x in kwargs.iteritems()]
    for key, value in new_args:
        args[key] = value
    return url_for(request.endpoint, **args)


def timeago(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return gettext("Just now")
        if second_diff < 60:
            return gettext('{s} seconds ago').format(s=str(second_diff))
        if second_diff < 120:
            return gettext("A minute ago")
        if second_diff < 3600:
            return gettext('{s} minutes ago').format(s=str(second_diff/60))
        if second_diff < 7200:
            return gettext("An hour ago")
        if second_diff < 86400:
            return gettext('{s} hours ago').format(s=str(second_diff/3600))
    if day_diff == 1:
        return gettext("Yesterday")
    if day_diff < 7:
        return gettext('{s} days ago').format(s=str(day_diff))
    if day_diff < 31:
        return gettext('{s} weeks ago').format(s=str(day_diff/7))
    if day_diff < 365:
        return gettext('{s} months ago').format(s=str(day_diff/30))
    return gettext('{s} years ago').format(s=str(day_diff/365))
