from flask import (
    Blueprint,
    render_template,
    request
)

from .constants import (
    BASIC_INFO,
    FEDERAL_INCOME,
    FEDERAL_INCOME_ADJUSTMENTS,
    BUSINESS_INCOME,
    FEDERAL_DEDUCTIONS,
    ESTIMATED_TAX_PAYMENTS
)

bp = Blueprint('main', __name__)

@bp.route('/')
def tax_form():
    categories = [
        BASIC_INFO,
        FEDERAL_INCOME,
        FEDERAL_INCOME_ADJUSTMENTS,
        BUSINESS_INCOME,
        FEDERAL_DEDUCTIONS,
        ESTIMATED_TAX_PAYMENTS
    ]
    return render_template('index.html', categories=categories)

@bp.route('/submit', methods=['POST'])
def submit_form():
    # first_name = request.form.get("first_name")
    # last_name = request.form.get("last_name")
    # full_name = "{} {}".format(first_name, last_name)

    # return render_template('index.html', name=full_name)
    return


@bp.route('/get', methods=['GET'])
def get_form_data():
    return

@bp.route('/download', methods=['GET'])
def download_pdf():
    return
