from django.urls import path
from . import views



# Setting the app_name value in order to be able to call app_name:view_name
app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
]
