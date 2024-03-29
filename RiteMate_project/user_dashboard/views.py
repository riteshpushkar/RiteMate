from django.shortcuts import render, redirect
from properties.models import listing
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required
def dashboard(request):
    # Filter listings based on the currently logged-in user
    try:
        data = listing.objects.filter(user=request.user)
    except Exception:
        data = listing.objects.all()
    return render(request, 'dashboard.html', {'data': data})

# @login_required
# def edit(request):
#     if request.method == "POST":
#         listing_id = request.POST.get('id')  # Fetching the ID from the form data
#         try:
#             data = listing.objects.get(pk=listing_id)
#         except listing.DoesNotExist:
#             # Handle the case where the listing does not exist
#             return render(request, 'edit.html', {'error': 'Listing not found'})
        
#         name = request.POST.get('name')
#         rent = request.POST.get('rent')
#         description = request.POST.get('description')
#         gender = request.POST.get('gender')
#         location = request.POST.get('location')
#         image = request.FILES.get('image')
        
#         if name:
#             data.name = name
#         if rent:
#             data.rent = rent
#         if description:
#             data.description = description
#         if gender:
#             data.gender = gender
#         if location:
#             data.location = location
#         if image:
#             data.image = image
        
#         data.save()
        
#         return render(request, 'edit.html', {'data': data})
#     else:
#         return render(request, 'edit.html')  # Return an empty form for GET requests

# @login_required
def delete(request, id):
    if request.method == "POST" :
        value_to_delete = listing.objects.filter(pk= id) 
        value_to_delete.delete()
        return redirect(request.path)
    data = listing.objects.all()
    return render(request, 'dashboard.html', {'data' : data})
        

def edit(request, id) :

    # to reflect old data in the frontend bas iske liye ye mehnat hai

    data = listing.objects.filter(pk=id)  # filter jo hai wo saare matching objects le aayega (bas error nahi dega), thats why we'll use first object only (get method is better option BTW in this case)
    
    listing_object = data[0]  # Accessing the first (and only) object in the queryset
    name = listing_object.name
    location = listing_object.location
    rent = listing_object.rent
    gender = listing_object.gender
    description = listing_object.description
    image = listing_object.image
    if listing_object.image2:
        image2 = listing_object.image2

    if listing_object.image3:
        image3 = listing_object.image3
        
    if listing_object.other_details :
        other_details = listing_object.other_details

    if listing_object.about_you :
        about_you = listing_object.about_you

    if listing_object.about_partner :
        about_partner = listing_object.about_partner

    
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        rent = request.POST.get('rent')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        try:
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            other_details = request.POST.get('other_details')
            about_you = request.POST.get('about_you')
            about_partner = request.POST.get('about_partner')
        except Exception as e:
            print(e)




        listing_obj = listing.objects.get(pk=id)
        
        listing_obj.name = name
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
        
        if other_details :
            listing_obj.other_details = other_details

        if about_you :
            listing_obj.about_you = about_you

        if about_partner :
            listing_obj.about_partner = about_partner
        
        
        listing_obj.save()
        return redirect('/dashboard/')
    return render(request, 'edit.html', {'name' : name, 'location' : location, 'rent' : rent, 'gender' : gender, 'description' : description, 'image' : image, 'other_details': other_details, 'about_you': about_you, 'about_partner' : about_partner, 'image2' : image2, 'image3': image3})

    