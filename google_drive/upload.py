from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

import auth

service = build( 'drive', 'v3', credentials=auth.get_service_account_cred() )

def upload_file(file, parent_id, mimetype= "text/plain"):
    file_metadata = {
        'name': os.path.basename(file), 
        "parents": [parent_id]
    }
    media = MediaFileUpload(file, mimetype=mimetype)
    Dfile = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return Dfile.get('id')