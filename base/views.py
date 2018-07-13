from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import MoleImage
from .forms import ImageForm

from .processing import actions, run_processor

from PIL import Image

import logging

def index(request):
    return render_page(request, ImageForm())

def render_page(request, form):
    images = MoleImage.objects.all()
    return render(request, "base/index.html", {
        'images': images,
        'form': form,
        'actions': actions,
    })

def upload_mole(request):
    form = ImageForm(request.POST, request.FILES)
    if not form.is_valid():
        return render_page(request, form)

    img = MoleImage(image = request.FILES['image'])
    img.save()

    return HttpResponseRedirect("/")

def process_mole(request, mole_id, action):
    args = {}
    for k, v in request.GET.items():
        args[k] = v

    img = MoleImage.objects.get(pk=mole_id)
    img = Image.open(img.image.file)
    img = run_processor(img, action, **args)
    if img is None :
        return Http404("unknown method")

    resp = HttpResponse(content_type="image/jpeg")
    img.save(resp, "JPEG")
    return resp
