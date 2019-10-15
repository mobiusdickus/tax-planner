# Tax Planner App

A simple flask app that redners a form that feeds into Google Sheets, merges with Google Docs, and finally exports the document to a PDF for download.

## Google APIs Requirements

In order to get this flask app up and running you will need to set a few things up from your google accounts developer console.

- Create a new project or use an existing one
- Enable Google Sheets API and Google Drive API
- Create a service account and download credentials in the form of a json file
- Enable domain wide delegation for said service account
- Authorize the client to the appropriate scopes from the Google Admin console

**Reference:**
- https://support.google.com/a/answer/7378726?hl=en
- https://developers.google.com/admin-sdk/directory/v1/guides/delegation

**Scopes:**
- https://www.googleapis.com/auth/drive
- https://www.googleapis.com/auth/drive.file
- https://www.googleapis.com/auth/spreadsheets

Once this is done, the service account's json credentials will have the ability to authenticate and act on behalf of the desired gsuite user to whom the master spreadhseet and master google doc belong. Make sure to save the json file as `client_secret.json`. You will need to base64 encode the `client_secret.json` and save the string as an environment variable.

Lastly, save the user account's email that you wish to house all your documents and save it as an environment variable.

**Environment Variables:**
- `CLIENT_SECRET_FILE`
- `PRIMARY_USER`

## Google App Requirements

Since this app utilizes Google Sheets, Google Docs, and Google Drive we will need a few pieces of information to ensure everything the app runs correctly.

### Google Drive

From the My Drive create a new folder (name doesn't matter), inside this Folder put the master spreadsheet and master doc. Inside the newly created folder create another folder (name doesn't matter), this is where all the copies (client files) will be stored.

We will now need to grab the folder Ids of both and set those as environment variables.

**Environment Variables:**
- `MASTER_FOLDER_ID`
- `CLIENT_FOLDER_ID`

### Google Sheets and Google Docs

Here we will also need to grab the sheets Id and the docs Id and set them as environment variables.

**Environment Variables:**
- `MASTER_SPREADSHEET_ID`
- `MASTER_DOC_ID`

## Prerequisites

- Install Docker & Docker Compose

## Local Development

Run with `make develop`.
