from django.conf import settings

import google.oauth2.credentials
import google_auth_oauthlib.flow



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
                include_granted_scopes='true')

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


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
