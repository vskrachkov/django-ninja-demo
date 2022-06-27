from django.contrib import admin
from django.urls import path

from api import api

admin.site.site_header = "ninja-demo"
admin.site.site_title = "ninja-demo"
admin.site.index_title = "ninja-demo"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
