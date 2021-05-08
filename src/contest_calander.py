from __future__ import print_function
import datetime
import os.path
from time import timezone
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import timezone

import json
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CALENDER_ID = 'iu1iul1u3n8ic3s78f4df15u4o@group.calendar.google.com'


def _getAllContests():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'src/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    file = open('src/contests.json', 'w')
    page_token = None
    # min_time = datetime.datetime.now(timezone.utc)
    min_time = datetime.datetime.now(
        timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(min_time)

    while True:
        events = service.events().list(
            calendarId=CALENDER_ID,
            timeMin=min_time,
            singleEvents=True, orderBy='startTime',
            pageToken=page_token
        ).execute()

        print(f'No of Contests: {len(events["items"])}')
        events_str = json.dumps(events['items'])
        file.write(events_str)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
