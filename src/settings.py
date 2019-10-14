import os
import sys


CLIENT_SECRET_FILENAME = '/tmp/client_secret.json'
CLIENT_SECRET_FILE = os.getenv('CLIENT_SECRET_FILE')
PRIMARY_USER = os.getenv('PRIMARY_USER')
MASTER_SPREADSHEET_ID = os.getenv('MASTER_SPREADSHEET_ID')
MASTER_DOC_ID = os.getenv('MASTER_DOC_ID')

if not all([CLIENT_SECRET_FILE, PRIMARY_USER,
            MASTER_SPREADSHEET_ID, MASTER_DOC_ID]):
    sys.exit('Environment not configured properly!')
