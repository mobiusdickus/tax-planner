from flask import (
    Blueprint,
    render_template,
    request
)

from .google import GoogleManager

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

@bp.route('/next')
def next_tab():
    return

@bp.route('/submit', methods=['POST'])
def submit_form():
    customer_name = request.form.get("first_name")

    new_spreadsheet = GoogleManager.copy_file(
        customer_name, 'spreadsheet'
    )

    updated_spreadsheet = GoogleManager.update_spreadsheet(
        new_spreadsheet
    )

    sheet_data = GoogleManager.get_sheet_data(
        updated_spreadsheet['id']
    )

    new_document = GoogleManager.copy_file(
        customer_name, 'document'
    )

    merged_document = GoogleManager.merge_doc(
        new_document, sheet_data
    )

    GoogleManager.export_pdf(merged_document)

    return render_template('index.html')

@bp.route('/download', methods=['GET'])
def download_pdf():
    return
