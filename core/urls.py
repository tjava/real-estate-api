from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core.settings.base import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Panel"
admin.site.index_title = "Welcome to Real Estate Admin Panel"