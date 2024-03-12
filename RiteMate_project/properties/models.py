from django.db import models

class listing(models.Model) :
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('any', 'Any')
    )
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 60)
    rent = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    description = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="RiteMate_project\media\properties_images")

