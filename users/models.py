from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

#Superuser
#Superpass1

#Username1
#password522

class User(AbstractUser):

    SALES = 'sales_member'
    MANAGEMENT = 'management_member'
    SUPPORT = 'support_member'
    ROLE_CHOICES = [
        (SALES, 'sales_member'),
        (MANAGEMENT, 'management_member'),
        (SUPPORT, 'support_member')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sales_contact')
