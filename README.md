# Tax Planner App

A simple flask app that redners a form that feeds into Google Sheets, merges with Google Docs, and finally exports the document to a PDF for download.

## Google APIs Requirements

In order to get this flask app up and running you will need to set a few things up from your google accounts developer console.

- Create a new project or use an existing one
- Enable Google Sheets API and Google Drive API
- Create a service account and download credentials in the form of a json file
- Enable domain wide delegation for said service account
- Authorize the client to the appropriate scopes from the Google Admin console

Reference:
- https://support.google.com/a/answer/7378726?hl=en
- https://developers.google.com/admin-sdk/directory/v1/guides/delegation

Scopes:
- https://www.googleapis.com/auth/drive
- https://www.googleapis.com/auth/drive.file
- https://www.googleapis.com/auth/spreadsheets

Once this is done the service account's json credentials will have the ability to authenticate and act on behalf of the desired gsuite user to whom the master spreadhseet and master google doc belong.

## Local Development

Run with `make develop`.
