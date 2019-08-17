from flask import Blueprint, request, render_template
from helpers.helper import is_blank

site_bp = Blueprint('site', __name__)

@site_bp.route('/', methods=['GET'])
def site_home_handler():
    name = request.args.get('name')
    if is_blank(name):
        name = 'world'

    return render_template('home.html', name=name)