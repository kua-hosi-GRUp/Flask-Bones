from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates')
group = Blueprint('group', __name__, template_folder='templates')
user = Blueprint('user', __name__, template_folder='templates')

import user_views
import group_views