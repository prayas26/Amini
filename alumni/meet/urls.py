from django.conf.urls import url
from django.conf.urls.static import static

from .views import (
    alumnus,
    )

urlpatterns = [
    url(r'^alumnus/', alumnus)
]