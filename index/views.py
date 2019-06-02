from django.shortcuts import render
from django.http import JsonResponse

from google_api.utils import youtube, utils



def index(request):
    if utils.is_authenticated(request):
        is_authenticated = True
        service = youtube.retrieve_authenticated_service(request.session['credentials'])
        playlists = youtube.my_playlists(service)

    return render(request, "index/index.html", locals())


def api_my_playlists(request):
    if utils.is_authenticated(request):
        service = youtube.retrieve_authenticated_service(request.session['credentials'])
        playlists = youtube.my_playlists(service)
        return JsonResponse({'playlists': playlists})

    return JsonResponse({'error': 'User not authenticated'})

def api_my_playlist_items(request):
    playlist_id = request.GET.get('playlist_id', None)
    if playlist_id and utils.is_authenticated(request):
        service = youtube.retrieve_authenticated_service(request.session['credentials'])
        playlist_items = youtube.my_playlist_items(service, playlist_id)
        return JsonResponse({'playlist_id': playlist_id, 'playlist_items': playlist_items})

    if playlist_id:
        return JsonResponse({'error': 'User not authenticated'})
    return JsonResponse({'error': 'Argument playlist_id not specified'})
