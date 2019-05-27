from django.shortcuts import render, redirect
from .utils.authentication import *



def authenticate(request):
    authorization_url, state = request_authorization_url()
    request.session['state'] = state
    return redirect(authorization_url)

def oauth2callback(request):
    if 'error' not in request.GET:
        state = request.session['state']
        credentials = retrieve_credentials(state, request.get_full_path())
        request.session['credentials'] = credentials_to_dict(credentials)

    return redirect('index:index')
