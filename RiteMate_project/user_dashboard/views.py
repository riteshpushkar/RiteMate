from django.shortcuts import render, redirect
from properties.models import listing
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

def dashboard(request):
    data = listing.objects.all()
    return render(request, 'dashboard.html', {'data': data})


def delete(request, id):
    if request.method == "POST" :
        value_to_delete = listing.objects.get(pk= id) 
        email = value_to_delete.email
        value_to_delete.delete()
        data = listing.objects.filter(email=email) 
        return render(request, 'dashboard.html', {'data':data})
    data = listing.objects.get(id=id)
    return render(request, 'dashboard.html', {'data' : data})


        

def edit(request, id):
    # Initialize variables with default values
    image2 = None
    image3 = None
    other_details = None
    about_you = None
    about_partner = None

    # Retrieve data from the database
    data = listing.objects.filter(pk=id)
    listing_object = data.first()  # Use first() instead of accessing index 0 directly

    # Assign values from the database to variables
    name = listing_object.name
    email = listing_object.email
    location = listing_object.location
    rent = listing_object.rent
    gender = listing_object.gender
    description = listing_object.description
    image = listing_object.image

    # Conditionally assign values to variables if they exist in the database object
    if listing_object.image2:
        image2 = listing_object.image2

    if listing_object.image3:
        image3 = listing_object.image3

    if listing_object.other_details:
        other_details = listing_object.other_details

    if listing_object.about_you:
        about_you = listing_object.about_you

    if listing_object.about_partner:
        about_partner = listing_object.about_partner

    if request.method == "POST":
        # Retrieve data from the form
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

        # Update the database object with the new data
        listing_obj = listing.objects.get(pk=id)
        listing_obj.name = name
        listing_obj.email = email
        listing_obj.location = location
        listing_obj.rent = rent
        listing_obj.gender = gender
        listing_obj.description = description

        if image:
            listing_obj.image = image

        if image2:
            listing_obj.image2 = image2

        if image3:
            listing_obj.image3 = image3

        if other_details:
            listing_obj.other_details = other_details

        if about_you:
            listing_obj.about_you = about_you

        if about_partner:
            listing_obj.about_partner = about_partner

        # Save the changes to the database
        listing_obj.save()
        data = listing.objects.filter(email=email)
        # Redirect to the dashboard page after saving
        return render(request, 'dashboard.html', {'data': data})
    
    # Pass variables to the template for rendering
    return render(request, 'edit.html', {'name': name, 'email': email, 'location': location, 'rent': rent, 'gender': gender, 'description': description, 'image': image, 'other_details': other_details, 'about_you': about_you, 'about_partner': about_partner, 'image2': image2, 'image3': image3})
