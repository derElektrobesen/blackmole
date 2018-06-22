from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views

import logging

urlpatterns = [
    url("mole/", views.upload_mole, name="upload_mole"),
    url("", views.index, name="home"),
]
