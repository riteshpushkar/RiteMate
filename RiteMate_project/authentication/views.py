from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from app.views import *
from .models import *
from app.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# from . views import listing
# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if details.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists, please try another.')
            return redirect(request.get_full_path())
        elif details.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists, please try another.')
            return redirect(request.get_full_path())
        else:
            hashed_password = make_password(password)
            new_user = details.objects.create(username=username, email=email, password=hashed_password)
            new_user.save()
            messages.success(request, 'Registered successfully!')
            return redirect(request.get_full_path())
        
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = details.objects.get(email=email)
        except details.DoesNotExist:
            messages.error(request, 'Invalid email')
            return render(request, 'login.html')
        
        # Verifying password
        if check_password(password, user.password):
            data = listing.objects.filter(email=email) 
            return render(request, 'test.html', {'data': data})
        else:
            messages.error(request, 'Invalid password')
            return render(request, 'login.html')

    return render(request, 'login.html')







# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         try:
#             user = listing.objects.get(email=email)
#         except listing.DoesNotExist:
#             messages.error(request, 'Invalid email')
#             return render(request, 'login.html', {'email': email})  # Pass email back to form

#         # Store user's email in session
#         request.session['user_email'] = email
#         return redirect('/dashboard/')  # Redirect to dashboard without passing email in URL

#     return render(request, 'login.html')












        # Retrieve user by email
    #     try:
    #         user = details.objects.get(email=email, password = hashed_password)
    #     except details.DoesNotExist:
    #         user = None

    #     if user is not None:
    #         # Check if provided password matches hashed password
    #         if check_password(password, user.password):
    #             # Fetch data related to the user
    #             data = listing.objects.filter(email=email)
    #             # Redirect to dashboard with data
    #             return redirect('/dashboard/', {'data': data})
    #         else:
    #             messages.warning(request, 'Invalid username or password. Please try again.')
    #             return redirect('/login/')  # Redirect to login page if authentication fails
    #     else:
    #         messages.warning(request, 'Invalid username or password. Please try again.')
    #         return redirect('/login/')  # Redirect to login page if user not found
    # else:
    #     return render(request, 'login.html')