from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(blank=True, default=0)  # cents
    # orders for document based dbs
    last_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # TODO: import and add user
    last_in = models.DateField(null=True, blank=True)
    folder_location = models.CharField(max_length=80, null=True, blank=True)

    needs_followup = models.BooleanField(default=False)
    updated = models.DateField(null=True, blank=True)

    created = models.DateField(null=True, blank=True)