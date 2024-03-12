from django.db import models

# Create your models here.
class issue(models.Model) :
    email = models.EmailField()
    message = models.TextField(max_length = 400)