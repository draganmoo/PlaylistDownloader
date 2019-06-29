from django.shortcuts import render
from django.http import JsonResponse

from mp3_tagger.utils import tagger



def api_tag_playlist(request):
    playlist_id = request.GET.get('playlist_id', None)
    if playlist_id:
        return JsonResponse({'result': tagger.tag_playlist(playlist_id)})

    return JsonResponse({'error': 'Argument playlist_id not specified'})
