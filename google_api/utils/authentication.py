from django.conf import settings

import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.oauth2.credentials import Credentials

import requests



def request_authorization_url():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                settings.GOOGLE_CLIENT_SECRETS_FILE,
                scopes=settings.YOUTUBE_SCOPE)

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required.
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
                # Enable offline access so that you can refresh an access token without
                # re-prompting the user for permission. Recommended for web server apps.
                access_type='offline',
                # Prompt the user to select an account.
                prompt='select_account',
                # Enable incremental authorization. Recommended as a best practice.
                include_granted_scopes='true',
                code_verifier='')

    return authorization_url, state


def retrieve_credentials(state, url):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                settings.GOOGLE_CLIENT_SECRETS_FILE,
                scopes=settings.YOUTUBE_SCOPE,
                state=state)
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI
    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    flow.fetch_token(authorization_response=url)

    return flow.credentials


def revoke_credentials(credentials):
    if 'token' in credentials:
        post_data = {'token': credentials['token']}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post('https://accounts.google.com/o/oauth2/revoke',
                                data=post_data, headers=headers)
        return response.status_code == requests.codes.ok

    return False


def is_valid_credentials(credentials):
    if 'token' in credentials:
        post_data = {'access_token': credentials['token']}
        response = requests.post('https://www.googleapis.com/oauth2/v1/tokeninfo',
                                data=post_data)
        return 'error' not in response.json()
    return False


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
