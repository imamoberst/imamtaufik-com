from flask import Blueprint, render_template

home_view = Blueprint('home_view', __name__)


@home_view.route('/')
def home():
    return render_template('home/index.html')
