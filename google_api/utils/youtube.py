from django.conf import settings

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials



def retrieve_authenticated_service(credentials_dict):
    cred = Credentials(credentials_dict["token"],
                refresh_token = credentials_dict["refresh_token"],
                token_uri = credentials_dict["token_uri"],
                client_id = credentials_dict["client_id"],
                client_secret = credentials_dict["client_secret"],
                scopes = credentials_dict["scopes"])
    return build(settings.YOUTUBE_API_SERVICE_NAME,
                settings.YOUTUBE_API_VERSION,
                credentials=cred)

def my_playlists(service, part='id, snippet'):
    response = service.playlists().list(part=part, mine=True, maxResults=50).execute()
    items = response['items']
    while 'nextPageToken' in response:
        response = service.playlist().list(part=part, mine=True, maxResults=50,
                        pageToken=response['nextPageToken']).execute()

        items += response['items']

    return items

def my_playlist_items(service, playlist_id, part='id, snippet, contentDetails'):
    response = service.playlistItems().list(part=part, playlistId=playlist_id, maxResults=50).execute()
    items = response['items']
    while 'nextPageToken' in response:
        response = service.playlistItems().list(part=part, playlistId=playlist_id, maxResults=50,
                        pageToken=response['nextPageToken']).execute()

        items += response['items']

    items = _remove_unavailable_items(items)
    return items


def _remove_unavailable_items(items):
    for item in items:
        if 'Private video' in item['snippet']['title']:     items.remove(item)
        elif 'Deleted video' in item['snippet']['title']:   items.remove(item)
    return items
