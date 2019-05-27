from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('google_api/', include('google_api.urls')),
]
