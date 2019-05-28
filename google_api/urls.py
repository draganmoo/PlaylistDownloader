from django.urls import path
from . import views



# Setting the app_name value in order to be able to call app_name:view_name
app_name = 'google_api'

urlpatterns = [
    path('', views.authenticate, name='index'),
    path('revoke_credentials/', views.revoke, name='revoke_credentials'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
]
