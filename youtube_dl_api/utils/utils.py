import os, zipfile



def compute_download_path(playlist_id):
    return os.path.join('media', playlist_id)

def compute_video_url(video_id):
    return 'https://www.youtube.com/watch?v={}'.format(video_id)


def generate_zip_file(response, playlist_id, playlist_title):
    path = compute_download_path(playlist_id)
    zip_file = zipfile.ZipFile(response, 'w')
    for root, dirs, files in os.walk(path):
        # File system modifications to produce the correct zip
        os.chdir('media')
        os.rename(playlist_id, playlist_title)
        for file in files:
            if file.endswith('.mp3'):
                zip_file.write(os.path.join(playlist_title, file))

        # Undo file system modifications
        os.rename(playlist_title, playlist_id)
        os.chdir('..')
    zip_file.close()
