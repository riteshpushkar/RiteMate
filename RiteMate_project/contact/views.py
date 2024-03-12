from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def contact(request) :
    if request.method == 'POST' :
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        message  = request.POST.get('message')

        contact_details = contact_us.objects.create(name = name, email = email, message = message)
        contact_details.save()
        messages.success(request, "Thanks for contacting, we'll get back to you shortly.")
        return redirect(request.get_full_path())
    return render(request, 'contact.html')






