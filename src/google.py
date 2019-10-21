import io
import os

from datetime import datetime
from apiclient import discovery
from apiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

from src import settings
from src.constants import (
    BASIC_INFO,
    FEDERAL_INCOME,
    FEDERAL_INCOME_ADJUSTMENTS,
    BUSINESS_INCOME,
    FEDERAL_DEDUCTIONS,
    ESTIMATED_TAX_PAYMENTS,

    MASTER_SHEET_RANGES,
    USE_FOR_PDF_SHEET_RANGES,
)



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
            os.getcwd(), self.client_secret_filename
        )

        credentials = service_account.Credentials.from_service_account_file(
            secret_file, scopes=self.scopes
        )
        delegated_credentials = credentials.with_subject(self.primary_user)

        return delegated_credentials

    def get_service(self, credentials, service_name, service_version):
        try:
            service = discovery.build(
                service_name, service_version, credentials=credentials
            )
        except OSError as e:
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
        # Get the Google Drive API service
        service = self.get_service(
            self.credentials, 'drive', 'v3'
        )

        # Prepare the request body params
        file_params = {
            # Name of the file to be copied
            'name': 'Tax Planner - {} - {}'.format(
                customer_name, datetime.now().replace(microsecond=0)
            ),
            # NOTE: Supposed to copy file to specified folder
            # 'parents': [{'id': self.copies_folder_id}]
        }

        # Accept alternative file ids for copy
        if not file_id:
            if file_type == 'spreadsheet':
                file_id = self.master_spreadsheet_id
            elif file_type == 'document':
                file_id = self.master_doc_id
            else:
                raise

        # Send file copy request
        response = service.files().copy(
            fileId=file_id, body=file_params
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
        for key, value in MASTER_SHEET_RANGES.items():
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
            elif key == 'ESTIMATED_TAX_PAYMENTS':
                category = ESTIMATED_TAX_PAYMENTS
            else:
                raise

            for r in value:
                data = {'category': key, 'range': r['range'], 'values': []}
                for field in category:
                    if r['pos'] == field['range_pos']:
                        data['values'].append(
                            [update_data[field['name']]]
                        )
                prepared_data.append(data)

        return prepared_data

    def update_spreadsheet(self, spreadsheet_id, update_data):
        # Get Google Sheets API service
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        # Prepare request body params
        request_data = []
        for d in update_data:
            request_data.append({
                'range': d['range'],
                'majorDimension': 'ROWS',
                'values': d['values']
            })

        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': request_data
        }

        # Send spreadsheet update request
        response = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body
        ).execute()

        return response

    def get_sheet_data(self, spreadsheet_id):
        # Get Google Sheets API service
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        # NOTE: Can loop over multiple ranges if applicable
        # Set the cell range for doc merge data
        cell_range = USE_FOR_PDF_SHEET_RANGES['DOC_MERGE'][0]['range']

        # Send spreadsheet get cell values request
        response = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=cell_range
        ).execute()

        # Create dict for row values
        rows = response.get('values', [])
        data = dict(zip(rows[0], rows[1]))

        return data

    def get_completion_data(self, document_id):
        completion_info = {
            'doc_link': 'https://docs.google.com/document/d/{}'.format(document_id),
            'pdf_link': '',
            'email_status': ''
        }

        # Set cell ranges for final spreadsheet update
        cell_range = USE_FOR_PDF_SHEET_RANGES['COMPLETION_INFO'][0]['range']

        # Prepare final spreadsheet data
        completion_data = [{
            'range': cell_range,
            'values': [[value for key, value in completion_info.items()]]
        }]

        return completion_data


    def merge_doc(self, document_id, data):
        # Get Google Docs API service
        service = self.get_service(
            self.credentials, 'docs', 'v1'
        )

        # Prepare request body params
        requests = []
        for key, value in data.items():
            requests.append({
                'replaceAllText': {
                    'containsText': {
                        'text': '{{%s}}' % key,
                        'matchCase': 'true'
                    },
                    'replaceText': value,
                }
            })

        body = {'requests': requests}

        # Send document merge request
        response = service.documents().batchUpdate(
            documentId=document_id, body=body
        ).execute()

        return response

    def export_pdf(self, document_id):
        # Get Google Drive API serivce
        service = self.get_service(self.credentials, 'drive', 'v3')

        # Send file download request and export to pdf
        request = service.files().export_media(
            fileId=document_id, mimeType='application/pdf'
        )

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()

        fh.seek(0)

        return fh
