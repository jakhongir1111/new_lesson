from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.views import index, detail
from djangoProject2 import settings

urlpatterns = [
    path('', index),
    path('post/<str:slug>', detail, name='detail'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
