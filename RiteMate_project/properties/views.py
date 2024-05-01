from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q


# Create your views here.
def display(request) :
    info = listing.objects.all()
    
    if 'search_for' in request.GET:
        search_for = request.GET.get('search_for')
        # print(search_for)
        
        data =  listing.objects.filter(
            Q(name__contains=search_for) |        
            Q(gender__contains=search_for) | 
            Q(description__contains=search_for) | 
            Q(location__contains=search_for)
        )

        return render(request, 'display.html', {'info': data})
    return render(request, 'display.html', {'info': info})


def properties(request) :
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        rent = request.POST.get('rent')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        other_details = request.POST.get('other_details')
        about_you = request.POST.get('about_you')
        about_partner = request.POST.get('about_partner')



        listing.objects.create(name = name,
                                       email=email,
                                       location = location, 
                                       rent = rent,
                                       gender = gender,
                                       description = description,
                                       image = image,
                                       image2 = image2,
                                       image3 = image3,
                                       other_details=other_details,
                                       about_you=about_you,
                                       about_partner=about_partner,
                                       )
        data = listing.objects.filter(email=email)
        return render(request, 'dashboard.html', {'data': data})
    return render(request, 'listing.html')



def card_details(request, id) :
    val = listing.objects.get(id=id)

    return render(request, 'card_details.html',{'card_val': val})
