# Google Calendar API Event Creator

This Python script allows users to interact with the Google Calendar API to create events programmatically. It utilizes OAuth 2.0 for authentication and authorization, enabling users to access their Google Calendar and create events with specified details.

Features

Authentication: The script handles authentication and authorization with the Google Calendar API using OAuth 2.0.
Event Creation: Users can create events with specified details such as summary, location, description, start and end times, recurrence rules, attendees, and reminders.
Token Management: User access and refresh tokens are stored in a file named token.json for future use.
Error Handling: The script includes error handling for HttpError exceptions that may occur during API requests.
Usage

Authorization Setup:
Before running the script, users need to set up their Google Cloud Platform project and create OAuth 2.0 credentials.
The credentials.json file containing OAuth 2.0 client ID and secret should be placed in the project directory.
Installation:
Install the required Python packages using pip install -r requirements.txt.
Execution:
Run the script by executing the main() function in the Python interpreter or using a Python IDE.
Follow the instructions to complete the OAuth 2.0 authorization flow.
Once authorized, the script will create events in the user's Google Calendar based on the provided details.
Customization:
Users can customize event details such as summary, location, description, start and end times, recurrence rules, attendees, and reminders by modifying the event dictionary in the script.
Dependencies

google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
Configuration

Credentials File: Ensure that the credentials.json file containing OAuth 2.0 client ID and secret is present in the project directory.
Token Storage: User access and refresh tokens are stored in a file named token.json. Ensure proper file permissions for token storage.
Notes

Users should review Google's API usage and quota limits to avoid any unexpected behavior.
Proper error handling should be implemented based on the application's requirements and use case scenarios.
