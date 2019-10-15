import io
import os
import datetime

from src import settings
from src.constants import (
    BASIC_INFO,
    FEDERAL_INCOME,
    FEDERAL_INCOME_ADJUSTMENTS,
    BUSINESS_INCOME,
    FEDERAL_DEDUCTIONS,
    ESTIMATED_TAX_PAYMENTS,

    MASTER_SPREADSHEET_RANGES
)

from apiclient import discovery
from apiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account



class Client(object):
    def __init__(self):
        self.client_secret_filename = settings.CLIENT_SECRET_FILENAME
        self.primary_user = settings.PRIMARY_USER
        self.scopes = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/spreadsheets"
        ]

    def _authenticate(self):
        secret_file = os.path.join(
            os.getcwd(),
            self.client_secret_filename
        )

        credentials = service_account.Credentials.from_service_account_file(
            secret_file,
            scopes=self.scopes
        )
        delegated_credentials = credentials.with_subject(self.primary_user)

        return delegated_credentials

    def get_service(self, credentials, service_name, service_version):
        try:
            service = discovery.build(
                service_name,
                service_version,
                credentials=credentials
            )
        except OSError as e:
            print(e)
            raise e

        return service


class GoogleManager(Client):
    def __init__(self):
        self.credentials = Client()._authenticate()
        self.master_spreadsheet_id = settings.MASTER_SPREADSHEET_ID
        self.master_doc_id = settings.MASTER_DOC_ID
        self.master_folder_id = settings.MASTER_FOLDER_ID
        self.client_folder_id = settings.CLIENT_FOLDER_ID

    def copy_file(self, customer_name, file_type, file_id=None):
        service = self.get_service(
            self.credentials, 'drive', 'v3'
        )

        file_params = {
            'name': 'Tax Planner - {} - {}'.format(
                customer_name, datetime.datetime.now()
            ),
            # NOTE: Supposed to copy file to specified folder
            # 'parents': [{'id': self.copies_folder_id}]
        }

        if not file_id:
            if file_type == 'spreadsheet':
                file_id = self.master_spreadsheet_id
            elif file_type == 'document':
                file_id = self.master_doc_id
            else:
                raise

        response = service.files().copy(
            fileId=file_id,
            body=file_params
        ).execute()

        # Move file into client folder
        service.files().update(
            fileId=response['id'],
            addParents=self.client_folder_id,
            removeParents=self.master_folder_id,
            fields='id, parents'
        ).execute()

        return response

    def prepare_update_data(self, update_data):
        prepared_data = []
        for key, value in MASTER_SPREADSHEET_RANGES.items():
            category = None
            if key == 'BASIC_INFO':
                category = BASIC_INFO
            elif key == 'FEDERAL_INCOME':
                category = FEDERAL_INCOME
            elif key == 'FEDERAL_INCOME_ADJUSTMENTS':
                category = FEDERAL_INCOME_ADJUSTMENTS
            elif key == 'BUSINESS_INCOME':
                category = BUSINESS_INCOME
            elif key == 'FEDERAL_DEDUCTIONS':
                category = FEDERAL_DEDUCTIONS
            elif 'ESTIMATED_TAX_PAYMENTS':
                category = ESTIMATED_TAX_PAYMENTS
            else:
                raise

            data = {'category': key, 'range': value['range'], 'values': []}
            for field in category:
                if value['pos'] == field['range_pos']:
                    data['values'].append(
                        update_data[field['name']]
                    )
            prepared_data.update(data)

        return prepared_data

    def update_spreadsheet(self, spreadsheet, update_data):
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        spreadsheet_id = spreadsheet['id']

        request_data = []
        for d in update_data:
            request_data.append({
                'range': d['range'],
                'majorDimension': 'ROWS',
                'values': d['values']
            })

        # ranges = MASTER_SPREADSHEET_RANGES
        # request_data = [
            # {       # Basic Info
                # 'range': ranges['BASIC_INFO'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['tax_advisor']],
                    # [update_data['client_name']],
                    # [update_data['business_name']],
                    # [update_data['state']],
                    # [update_data['filing_status']]
                # ]
            # }, {
                # 'range': ranges['BASIC_INFO'][1],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['industry']]
                # ]
            # }, {
                # 'range': ranges['BASIC_INFO'][2],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['num_of_children']]
                # ]
            # }, {    # Federal Income
                # 'range': ranges['FEDERAL_INCOME'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['w2_income']],
                    # [update_data['bank_interest']],
                    # [update_data['taxable_ira_dist']],
                    # [update_data['ordinary_dividends']],
                    # [update_data['qualified_dividends']],
                    # [update_data['short_term_cap_gains']],
                    # [update_data['long_term_cap_gains']],
                    # [update_data['other_income']]
                # ]
            # }, {    # Federal Income Adjustments
                # 'range': ranges['FEDERAL_INCOME_ADJUSTMENTS'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['health_insurance_premium']],
                    # [update_data['sep_ira_contribution']],
                    # [update_data['ira_deduction']],
                    # [update_data['401k_contribution']],
                    # [update_data['alimony_paid']],
                    # [update_data['other_deductions']]
                # ]
            # }, {    # Business Income
                # 'range': ranges['BUSINESS_INCOME'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['s_corp_business_income']],
                    # [update_data['schedule_c_income']],
                    # [update_data['s_corp_wages']]
                # ]
            # }, {    # Federal Deductions
                # 'range': ranges['FEDERAL_DEDUCTIONS'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['mortgage_interest']],
                    # [update_data['state_income_taxes']],
                    # [update_data['local_city_income_taxes']],
                    # [update_data['property_taxes']],
                    # [update_data['personal_property_taxes']],
                    # [update_data['cash_donations']],
                    # [update_data['noncash_donations']],
                    # [update_data['other_donations']],
                    # [update_data['medical_and_dental']]
                # ]
            # }, {
                # 'range': ranges['FEDERAL_DEDUCTIONS'][1],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['federal_tax_withheld']]
                # ]
            # }, {    # ESTIMATED_TAX_PAYMENTS
                # 'range': ranges['ESTIMATED_TAX_PAYMENTS'][0],
                # 'majorDimension': 'ROWS',
                # 'values': [
                    # [update_data['federal_estimated_tax_payments']]
                # ]
            # }
        # ]

        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': request_data
        }

        response = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()

        return response

    def get_sheet_data(self, spreadsheet_id):
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        value_range = "'Useforpdf'!A1:O2"

        response = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=value_range
        ).execute()
        rows = response.get('values', [])

        # Create dict for row values
        data = dict(zip(rows[0], rows[1]))

        return data

    def merge_doc(self, document, data):

        service = self.get_service(
            self.credentials, 'docs', 'v1'
        )

        requests = []
        for key, value in data.items():
            requests.append({
                'replaceAllText': {
                    'containsText': {
                        'text': '{{%s}}' % key,
                        'matchCase':  'true'
                    },
                    'replaceText': value,
                }
            })

        result = service.documents().batchUpdate(
            documentId=document['id'],
            body={'requests': requests}
        ).execute()

        return result

    def export_and_download_pdf(self, document_id):
        service = self.get_service(
            self.credentials, 'drive', 'v3'
        )
        request = service.files().export_media(
            fileId=document_id,
            mimeType='application/pdf'
        )

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        fh.seek(0)

        return fh
