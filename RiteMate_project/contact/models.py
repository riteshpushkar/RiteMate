from django.db import models

class contact_us(models.Model) :
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.CharField(max_length = 300)
