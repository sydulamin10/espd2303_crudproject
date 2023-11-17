from django.shortcuts import render, redirect
from create.models import profile
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == 'GET':
        search = request.GET.get('src')
        if search:
            prof = profile.objects.filter(Q(name__icontains=search) | Q(email__icontains=search))
            if not prof:
                messages.error(request, "No Profile Found.")
                return redirect('home')
        else:
            prof = profile.objects.all()
    return render(request, 'Home/home.html', locals())
