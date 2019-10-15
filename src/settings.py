import os
import sys


MASTER_SPREADSHEET_RANGES = {
    'BASIC_INFO': [
        "'Master Sheet'!B2:B6",
        "'Master Sheet'!G2",
        "'Master Sheet'!G6",
    ],
    'FEDERAL_INCOME': [
        "'Master Sheet'!B9:B16",
    ],
    'FEDERAL_INCOME_ADJUSTMENTS': [
        "'Master Sheet'!B19:B24",
    ],
    'BUSINESS_INCOME': [
        "'Master Sheet'!B27:B29",
    ],
    'FEDERAL_DEDUCTIONS': [
        "'Master Sheet'!G11:G19",
        "'Master Sheet'!G23"
    ],
    'ESTIMATED_TAX_PAYMENTS': [
        "'Master Sheet'!G26",
    ]
}

CLIENT_SECRET_FILENAME = '/tmp/client_secret.json'
CLIENT_SECRET_FILE = os.getenv('CLIENT_SECRET_FILE')
PRIMARY_USER = os.getenv('PRIMARY_USER')
MASTER_SPREADSHEET_ID = os.getenv('MASTER_SPREADSHEET_ID')
MASTER_DOC_ID = os.getenv('MASTER_DOC_ID')
MASTER_FOLDER_ID = os.getenv('MASTER_FOLDER_ID')
CLIENT_FOLDER_ID = os.getenv('CLIENT_FOLDER_ID')

if not all([CLIENT_SECRET_FILE, PRIMARY_USER,
            MASTER_SPREADSHEET_ID, MASTER_DOC_ID,
            MASTER_FOLDER_ID, CLIENT_FOLDER_ID]):
    sys.exit('Environment not configured properly!')
