import os
import datetime

from apiclient import discovery
from google.oauth2 import service_account


class Client(object):
    def __init__(self):
        # NOTE: Use ENV vars
        self.client_secret_file = 'client_secret.json'
        self.primary_user = 'colin@tastecreme.com'
        self.scopes = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/spreadsheets"
        ]

    def _authenticate(self):
        secret_file = os.path.join(
            os.getcwd(),
            self.client_secret_file
        )

        credentials = service_account.Credentials.from_service_account_file(
            secret_file,
            scopes=self.scopes
        )

        return credentials

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
        # NOTE: Use ENV vars
        self.credentials = Client._authenticate()
        self.master_spreadsheet_id = ''
        self.master_doc_id = ''

    def copy_file(self, customer_name, file_id):
        service = self.get_service(
            self.credentials, 'drive', 'v3'
        )

        file_params = {
            'name': 'Tax Planner - {} - {}'.format(
                customer_name, datetime.now()
            )
        }
        response = service.files().copy(
            fileId=file_id,
            body=file_params
        ).execute()

        return response

    def update_spreadsheet(self, spreadsheet):
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        spreadsheet_id = spreadsheet['id']

        update_data = {
            'valueInputOption': 'USER_ENTERED',
            'data': []
        }

        response = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=update_data
        ).execute()

        return response

    def get_sheet_data(self, spreadsheet_id):
        service = self.get_service(
            self.credentials, 'sheets', 'v4'
        )

        value_range = "'Useforpdf'!A2:O2"

        response = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=value_range
        ).execute()
        rows = response.get('values', [])

        return rows

    def merge_doc(self, document, data):

        service = self.get_service(
            self.credentials, 'docs', 'v1'
        )

        requests = [{
            'replaceAllText': {
                'containsText': {
                    'text': '{{customer-name}}',
                    'matchCase':  'true'
                },
                'replaceText': data['customer_name'],
            }}, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{date}}',
                    'matchCase':  'true'
                },
                'replaceText': data['date'],
            }
        }]

        result = service.documents().batchUpdate(
            documentId=document['id'],
            body={'requests': requests}
        ).execute()

        return result
