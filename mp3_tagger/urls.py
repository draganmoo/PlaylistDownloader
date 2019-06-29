from django.urls import path
from . import views



# Setting the app_name value in order to be able to call app_name:view_name
app_name = 'mp3_tagger'

urlpatterns = [
    path('tag_playlist/', views.api_tag_playlist, name='tag_playlist'),
]
