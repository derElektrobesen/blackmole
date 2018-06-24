# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse

from .models import MoleImage
from .forms import ImageForm

def index(request):
    return render_page(request, ImageForm())

def render_page(request, form):
    images = MoleImage.objects.all()
    return render(request, "base/index.html", {
        'images': images,
        'form': form,
    })

def upload_mole(request):
    form = ImageForm(request.POST, request.FILES)
    if not form.is_valid():
        return render_page(request, form)

    img = MoleImage(image = request.FILES['image'])
    img.save()

    return HttpResponseRedirect("/")

def process_mole(request, moleid):
    return HttpResponse("XXX")
