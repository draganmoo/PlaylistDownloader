from django.shortcuts import render

from google_api.utils import youtube
from google_api.utils.authentication import is_valid_credentials


def index(request):
    is_authenticated = 'credentials' in request.session and \
                        is_valid_credentials(request.session['credentials'])
    if is_authenticated:
        service = youtube.retrieve_authenticated_service(request.session['credentials'])
        playlists = youtube.my_playlists(service)

    return render(request, "index/index.html", locals())
