from django.shortcuts import render, redirect
from .models import issue
from django.contrib import messages

def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message_content = request.POST.get('message')  # Avoid using 'message' as it's the name of the model field
        new_issue = issue(email=email, message=message_content)
        new_issue.save()
        messages.success(request, "MESSAGE SENT SUCCESSFULLY")
        return redirect('/')
    return render(request, 'index.html')
