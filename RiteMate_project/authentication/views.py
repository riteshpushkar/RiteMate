from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from app.views import *
# Create your views here.

def user_signup(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = User.objects.create_user(first_name = 'test', last_name = 'ing', username = username, email = email, password = password)
        data.save()
        return redirect('/login')
    return render(request, 'signup.html')




def user_login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user :
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login.html')