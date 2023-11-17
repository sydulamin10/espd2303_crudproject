from django.shortcuts import render
from create.models import profile


# Create your views here.
def read(request, id):
    prof = profile.objects.get(id=id)
    return render(request, 'read/read.html', locals())
