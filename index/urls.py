from django.urls import path
from . import views



# Setting the app_name value in order to be able to call app_name:view_name
app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_playlists', views.api_my_playlists, name='my_playlists'),
    path('my_playlist_items', views.api_my_playlist_items, name='my_playlist_items'),
]
