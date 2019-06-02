import os, youtube_dl



def _gen_ydl_opts(path):
    return {'format': 'bestaudio/best',
                'postprocessors': [{'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': '192'}],
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'writethumbnail': True}


def download_url(url, path):
    try:
        with youtube_dl.YoutubeDL(_gen_ydl_opts(path)) as ydl:
            ydl.download([url])
            return True
    except:
        return False
    return False
