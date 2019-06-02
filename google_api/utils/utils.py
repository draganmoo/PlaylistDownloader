from google_api.utils.authentication import is_valid_credentials



def is_authenticated(request):
    return 'credentials' in request.session and \
                is_valid_credentials(request.session['credentials'])
