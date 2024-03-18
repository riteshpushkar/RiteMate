from django.shortcuts import render, redirect
from .models import issue
from django.contrib import messages
from properties.models import listing
from django.db.models import Q

def home(request):

    if request.method == "POST":
        email = request.POST.get('email')
        message_content = request.POST.get('message')  # Avoid using 'message' as it's the name of the model field
        new_issue = issue(email=email, message=message_content)
        new_issue.save()
        messages.success(request, "MESSAGE SENT SUCCESSFULLY")
        return redirect('/')
    

    if 'search_for' in request.GET:
        search_for = request.GET.get('search_for')
        # print(search_for)
        
        data =  listing.objects.filter(
            Q(name__contains=search_for) | Q(gender__contains=search_for) | Q(description__contains=search_for) | Q(location__contains=search_for)
        )

        return render(request, 'display.html', {'info': data})
    return render(request, 'index.html')

