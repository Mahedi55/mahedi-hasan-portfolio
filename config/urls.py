from django.contrib import admin
from django.urls import path

from portfolio.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
