from django.shortcuts import render, HttpResponseRedirect
from create.models import profile
from django.contrib import messages
import os


def delete(request, id):
    prof = profile.objects.get(id=id)
    if not prof.image == 'def.png':
        os.remove(prof.image.path)
    prof.delete()

    messages.warning(request, "Profile Deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
