from django.shortcuts import render
from .models import *

# Create your views here.
def display(request) :
    info = listing.objects.all()
    return render(request, 'display.html', {'info': info})


def properties(request) :
    if request.method == 'POST' :
        name = request.POST.get('name')
        location = request.POST.get('location')
        rent = request.POST.get('rent')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        listing.objects.create(name = name, 
                                       location = location, 
                                       rent = rent,
                                       gender = gender,
                                       description = description,
                                       image = image)
        



    return render(request, 'listing.html')






