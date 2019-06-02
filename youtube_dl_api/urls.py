from django.urls import path
from . import views



# Setting the app_name value in order to be able to call app_name:view_name
app_name = 'youtube_dl_api'

urlpatterns = [
    path('youtube_dl/download_video/', views.api_server_download_video, name='server_download_video'),

    path('client/download_playlist/zip', views.client_playlist_zip, name='client_playlist_zip'),
]
