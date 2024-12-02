from django.contrib import admin
from django.urls import include, path

from settings.api_router import router_v1

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/", include(router_v1.urls)),
]
