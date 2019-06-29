from youtube_dl_api.utils.utils import compute_download_path

from spacy_api.utils.recognizer import load_nlp, recognize_entities_from_raw

import eyed3, os



def tag_playlist(playlist_id):
    dir = compute_download_path(playlist_id)
    nlp = load_nlp(os.path.join('spacy_api', os.path.join('spacy_models', 'model')))
    if os.path.isdir(dir):
        os.chdir(dir)
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.mp3'):
                    recognition = recognize_entities_from_raw(nlp, file[:-4])
                    _complete_tag_from_dic(file, recognition)
        os.chdir('../..')
        return True

    return False


def _complete_tag_from_dic(file, recognition):
    audiofile = eyed3.load(file)
    if 'TITLE' in recognition:
        audiofile.tag.title = recognition['TITLE']
    if 'AUTHORS' in recognition:
        audiofile.tag.artist = recognition['AUTHORS']
    audiofile.tag.save()
