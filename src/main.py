from flask import (
    Blueprint,
    render_template,
    request,
    send_file
)

from .google import GoogleManager
from .constants import (
    BASIC_INFO,
    FEDERAL_INCOME,
    FEDERAL_INCOME_ADJUSTMENTS,
    BUSINESS_INCOME,
    FEDERAL_DEDUCTIONS,
    ESTIMATED_TAX_PAYMENTS,

    STATES,
    FILING_STATUSES,
    INDUSTRIES
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
    return render_template('index.html', categories=categories,
                           states=STATES, industries=INDUSTRIES,
                           filing_statuses=FILING_STATUSES)

@bp.route('/submit', methods=['POST'])
def submit_form():
    manager = GoogleManager()
    form_data = request.form
    customer_name = form_data['client_name']

    new_spreadsheet = manager.copy_file(
        customer_name, 'spreadsheet'
    )

    prepared_data = manager.prepare_update_data(form_data)

    updated_spreadsheet = manager.update_spreadsheet(
        new_spreadsheet,
        prepared_data
    )

    sheet_data = manager.get_sheet_data(
        updated_spreadsheet['spreadsheetId']
    )

    new_document = manager.copy_file(
        customer_name, 'document'
    )

    merged_document = manager.merge_doc(
        new_document, sheet_data
    )

    file = manager.export_pdf(merged_document['documentId'])

    return send_file(
        file,
        attachment_filename=new_document['name'],
        as_attachment=False,
        mimetype='application/pdf'
    )
