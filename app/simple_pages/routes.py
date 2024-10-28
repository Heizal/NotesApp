from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)
# Home route
@blueprint.route('/')
def index():
    return render_template('home.html')

# contact route
@blueprint.route('/contact')
def contact():
    return render_template('contact.html')