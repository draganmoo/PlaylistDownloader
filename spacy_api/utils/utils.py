from django.conf import settings

import csv, requests



LABELS = ('RAW', 'TITLE', 'AUTHOR')

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

    return raw_data


def save_data_to_csv(file, data, delimiter=','):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerow(LABELS)
        for row in data:
            writer.writerow(tuple([row[key] for key in LABELS]))

def read_data_from_csv(file, delimiter=','):
    data = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return row
