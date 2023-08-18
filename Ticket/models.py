from django.db import models

class users(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
class tickets(models.Model):
    ticketid = models.CharField(max_length=255)
    ticket_date = models.DateField()
    username = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # image = models.ImageField()

