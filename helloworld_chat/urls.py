# helloworld-chat/helloworld_chat_app/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("helloworld.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
