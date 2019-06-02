from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('google_api/', include('google_api.urls')),
    path('youtube_dl_api/', include('youtube_dl_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
