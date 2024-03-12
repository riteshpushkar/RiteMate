"""RiteMate_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import *
from contact.views import *
from properties.views import *
from user_dashboard.views import *
from payment.views import *

from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', user_login),
    path('signup/', user_signup),
    path('contact/', contact),
    path('properties/', properties),
    path('display/', display),
    path('dashboard/', dashboard),
    path('payment/', payment),
    path('delete/<int:id>/', delete, name='deletedata'),
    path('<int:id>/', edit, name='editdata'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
