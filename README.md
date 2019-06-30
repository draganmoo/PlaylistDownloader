# PlaylistDownloader

Local website in order to download MP3 files of all playlist of your YouTube account easily.

## Getting Started

### Configuration

You will need to create yourself an account on the following [link](https://console.developers.google.com) in order to access the YouTube data API.
Once the account and the project created you will need to create two keys:
- 1 API key
- 1 OAuth 2.0 client ID (specify http://localhost:8000/google_api/oauth2callback for the redirection URI)

With all those informations you will need to edit the configurations files accordingly.
Lastly, you will need to generate a new Django secret key and edit the configuration file. A new key can be generated with the following commands on a python console:

```
import random
''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
```

### Prerequisites

In order to run the project you need to install python3 + pipenv. Commands to download them can be easily found on Internet.
Once pipenv installed, you only need to type the following two commands. The first one is needed to include thumbnails in the MP3 file.

```
brew install ffmpeg
pipenv install
```

### Launch the server locally

The server can be launched easily on local by typing the following commands:

```
python3 manage.py migrate
python3 manage.py runserver
```

## Mainly Built With

* [YouTube-dl](https://github.com/ytdl-org/youtube-dl) - The python package to download from YouTube
