from django.contrib.auth.models import User
from django.db import models

class listing(models.Model) :
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('any', 'Any')
    )
    name = models.CharField(max_length = 40)
    location = models.CharField(max_length = 200)
    rent = models.IntegerField()
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default = 'Any')
    description = models.CharField(max_length = 800)
    image = models.ImageField(upload_to="properties_images")
    
    
    
    image2 = models.ImageField(upload_to="properties_images", null=True)
    image3 = models.ImageField(upload_to="properties_images", null=True)
    other_details = models.CharField(max_length = 800, null=True)
    about_you = models.CharField(max_length = 800, null=True)
    about_partner = models.CharField(max_length = 800, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



