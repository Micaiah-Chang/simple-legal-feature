from django.conf.urls import include, url
from django.contrib import admin

from views import changeset_route

urlpatterns = [
    url(r'$', changeset_route),
]
