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
    INDUSTRIES,

    USE_FOR_PDF_SHEET_RANGES,
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

    # Create client spreadsheet from master spreadsheet
    new_spreadsheet = manager.copy_file(
        customer_name, 'spreadsheet'
    )

    # Prepare form data for client spreadsheet
    prepared_data = manager.prepare_update_data(form_data)

    # Update client spreadsheet data
    updated_spreadsheet = manager.update_spreadsheet(
        new_spreadsheet['id'], prepared_data
    )

    # Get spreadsheet data for pdf
    sheet_data = manager.get_sheet_data(
        updated_spreadsheet['spreadsheetId']
    )

    # Create client doc from master doc
    new_document = manager.copy_file(
        customer_name, 'document'
    )

    # Merge client spreadsheet data with client doc
    merged_document = manager.merge_doc(
        new_document['id'], sheet_data
    )

    # Get final step completion info
    completion_data = manager.get_completion_data(
        new_document['id']
    )

    # Update spreadhseet with completion info (links)
    manager.update_spreadsheet(
        new_spreadsheet['id'], completion_data
    )

    # Download client doc and export as pdf
    file = manager.export_pdf(merged_document['documentId'])

    return send_file(
        file,
        attachment_filename=new_document['name'],
        as_attachment=False,
        mimetype='application/pdf'
    )
