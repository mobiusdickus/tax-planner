from flask import (
    Blueprint,
    render_template,
    request
)

bp = Blueprint('main', __name__)

@bp.route('/')
def tax_form():
    return render_template('index.html')

@bp.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    full_name = "{} {}".format(first_name, last_name)

    return render_template('index.html', name=full_name)

@bp.route('/get', methods=['GET'])
def get_form_data():
    return
