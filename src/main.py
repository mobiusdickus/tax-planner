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
    return render_template('index_bs.html', categories=categories)


@bp.route('/next')
def next_tab():
    return

@bp.route('/submit', methods=['POST'])
def submit_form():
    manager = GoogleManager()
    update_data = request.form
    customer_name = update_data['client_name']

    new_spreadsheet = manager.copy_file(
        customer_name, 'spreadsheet'
    )

    print(new_spreadsheet)

    updated_spreadsheet = manager.update_spreadsheet(
        new_spreadsheet,
        update_data
    )

    print(updated_spreadsheet)

    sheet_data = manager.get_sheet_data(
        updated_spreadsheet['spreadsheetId']
    )

    print(sheet_data)

    new_document = manager.copy_file(
        customer_name, 'document'
    )

    print(new_document)

    merged_document = manager.merge_doc(
        new_document, sheet_data
    )

    print(merged_document)

    pdf_request = manager.export_pdf(merged_document['documentId'])

    return render_template('index.html', data=update_data)

@bp.route('/download', methods=['GET'])
def download_pdf():
    return
