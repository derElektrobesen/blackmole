from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import MoleImage
from .forms import ImageForm

from .processing import MoleImage as ImageProcessor

from PIL import Image

import logging

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

def process_mole(request, mole_id):
    img = MoleImage.objects.get(pk=mole_id)
    img = Image.open(img.image.file)
    img = ImageProcessor(img).process()
    resp = HttpResponse(content_type="image/gif")
    img.save(resp, "JPEG")
    return resp
