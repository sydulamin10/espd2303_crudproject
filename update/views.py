from django.shortcuts import render, redirect
from create.models import profile
from django.contrib import messages
import os


# Create your views here.
def update(request, id):
    prof = profile.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        date_of_birth = request.POST.get('date_of_birth')

        if not name:
            messages.error(request, "input name please.")
        elif not email:
            messages.error(request, "input email please.")
        elif not address:
            messages.error(request, "input address please.")
        elif not phone_number:
            messages.error(request, "input phone_number please.")
        elif not date_of_birth:
            messages.error(request, "input date_of_birth please.")
        else:
            if image:
                if not prof.image == 'def.png':
                    os.remove(prof.image.path)
                new_prof = prof(name=name, email=email, image=image, address=address,
                                phone_number=phone_number,
                                gender=gender, religion=religion, date_of_birth=date_of_birth)
                new_prof.save()
                messages.success(request, "Profile details updated.")
                return redirect('home')
            else:
                new_prof = prof(name=name, email=email, address=address,
                                phone_number=phone_number,
                                gender=gender, religion=religion, date_of_birth=date_of_birth)
                new_prof.save()
                messages.success(request, "Profile details updated.")
                return redirect('home')
    return render(request, 'update/update.html', locals())


def palash():
    pass+


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
