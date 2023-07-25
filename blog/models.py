from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    