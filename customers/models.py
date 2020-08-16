from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=150,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    lga = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=400,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name