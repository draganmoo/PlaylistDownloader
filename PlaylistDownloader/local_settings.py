import os

# In order to enable https callback from google
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Google App settings
GOOGLE_CLIENT_SECRETS_FILE = 'configuration/client_secret.json'
if not os.path.isfile(GOOGLE_CLIENT_SECRETS_FILE):
    raise Exception('A configuration/client_secret.json is required to run this project !')

GOOGLE_REDIRECT_URI = 'http://localhost:8000/google_api/oauth2callback'
YOUTUBE_SCOPE = ['https://www.googleapis.com/auth/youtube.readonly']
