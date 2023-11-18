from django.shortcuts import render, redirect
from create.models import profile
from django.contrib import messages
import os


def update(request, id):
    prof = profile.objects.get(id=id)

    if request.method == 'POST':
        # save data direct to object and then save to database
        prof.name = request.POST.get('name')
        prof.email = request.POST.get('email')
        new_image = request.FILES.get('image')
        prof.address = request.POST.get('address')
        prof.phone_number = request.POST.get('phone_number')
        prof.gender = request.POST.get('gender')
        prof.religion = request.POST.get('religion')
        prof.date_of_birth = request.POST.get('date_of_birth')

        if not all([prof.name, prof.email, prof.address, prof.phone_number, prof.date_of_birth]):
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'update/update.html', locals())
        # start my logic to replace new image with old image and then delete old image path
        if prof.image:
            old_image_path = prof.image.path
            if old_image_path and os.path.exists(old_image_path):
                os.remove(old_image_path)
                prof.image = new_image
            
            prof.save()
            messages.success(request, "Profile details updated.")
            return redirect('home')

    return render(request, 'update/update.html', locals())
