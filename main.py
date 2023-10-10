import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
    """Shows basic usage of the Google Calendar API. 
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    # The file token.json stores the user's access and refresh tokens and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/zahra/Desktop/Projects01/Calender-autopy/credentials.json', SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Code to show the start and name of the next 10 events can be added here

        event = {
            'summary': 'event',
            'location': 'online',
            'description': 'idk something nice',
            'start': {
                'dateTime': '2023-10-28T09:00:00-04:00',  # Adjusted time for 'America/Toronto'
                'timeZone': 'America/Toronto',
            },
            'end': {
                'dateTime': '2023-10-28T17:00:00-04:00',  # Adjusted time for 'America/Toronto'
                'timeZone': 'America/Toronto',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")

    except HttpError as error:
        print("An error has occurred: ", error)


if __name__ == "__main__":
    main()
