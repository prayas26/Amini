from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include("meet.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)