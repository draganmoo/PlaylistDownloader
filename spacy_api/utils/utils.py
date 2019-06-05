from django.conf import settings

import requests, pandas as pd



LABELS = ['RAW', 'TITLE', 'AUTHORS', 'FEAT', 'REMIX', 'TRASH']

def retrieve_raw_data(playlist_id):
    raw_data = []
    params = {'part': 'snippet', 'maxResults': 50,
                'playlistId': playlist_id, 'key': settings.API_KEY}
    response = requests.get('https://www.googleapis.com/youtube/v3/playlistItems',
                            params=params)
    for item in response.json()['items']:
        row = {key: '' for key in LABELS}
        row['RAW'] = item['snippet']['title']
        raw_data.append(row)

    return pd.DataFrame(raw_data, columns=LABELS)


def save_dataframe_to_csv(file, dataframe, delimiter=';'):
    dataframe.to_csv(file, sep=delimiter)

def read_dataframe_from_csv(file, delimiter=';'):
    dataframe = pd.read_csv(file, sep=delimiter, names=LABELS)
    dataframe.where(dataframe.notnull(), None)
    return dataframe
