def compute_download_path(playlist_id):
    return 'media/{}'.format(playlist_id)

def compute_video_url(video_id):
    return 'https://www.youtube.com/watch?v={}'.format(video_id)
