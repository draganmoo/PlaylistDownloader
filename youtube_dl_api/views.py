from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from youtube_dl_api.utils import downloader, utils



def api_server_download_video(request):
    playlist_id = request.GET.get('playlist_id', None)
    video_id = request.GET.get('video_id', None)
    if playlist_id and video_id:
        path = utils.compute_download_path(playlist_id)
        url = utils.compute_video_url(video_id)
        return JsonResponse({'result': downloader.download_url(url, path)})

    if playlist_id:
        return JsonResponse({'error': 'Argument video_id not specified'})
    return JsonResponse({'error': 'Argument playlist_id not specified'})


@transaction.atomic()
def client_playlist_zip(request):
    playlist_id = request.GET.get('playlist_id', None)
    playlist_title = request.GET.get('playlist_title', None)
    if playlist_id and playlist_title:
        response = HttpResponse(content_type='application/zip')
        utils.generate_zip_file(response, playlist_id, playlist_title)
        response['Content-Disposition'] = 'attachment; filename={}.zip'.format(playlist_title)
        return response

    if playlist_id:
        return JsonResponse({'error': 'Argument playlist_title not specified'})
    return JsonResponse({'error': 'Argument playlist_id not specified'})
