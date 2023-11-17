from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import profile


# Create your views here.

def create(request):
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
            # if profile.objects.filter(name=name).exists():
            #     messages.warning(request, "Profile name already taken.")
            #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # else:
            #     if name:
            #         number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '*', '&', '^', '%',
            #                   '$', '#', '@', '!']
            #         for i in name:
            #             if i in number:
            #                 messages.warning(request, "Profile name contain number.")
            #                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #     else:
            if image:
                prof = profile.objects.create(name=name, email=email, image=image, address=address,
                                              phone_number=phone_number,
                                              gender=gender, religion=religion, date_of_birth=date_of_birth)
                prof.save()
                messages.success(request, "Profile details updated.")
                return redirect('home')
            else:
                prof = profile.objects.create(name=name, email=email, address=address,
                                              phone_number=phone_number,
                                              gender=gender, religion=religion, date_of_birth=date_of_birth)
                prof.save()
                messages.success(request, "Profile details updated.")
                return redirect('home')

    return render(request, 'create/create.html')
