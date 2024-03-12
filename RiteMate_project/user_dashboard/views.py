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
    data = listing.objects.filter(pk=id)
    
    return render(request, 'edit.html', {'data' : data})
    