from django.conf import settings
from django.urls import path, include
from . import views

import logging

urlpatterns = [
    path("mole/", views.upload_mole, name="upload_mole"),
    path("mole/<int:mole_id>/process", views.process_mole, name="process_mole"),
]

urlpatterns += [
    path("", views.index, name="home"),
]
