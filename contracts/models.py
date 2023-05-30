from django.db import models
from users.models import Client
from django.contrib.auth.models import User


class Contract(models.Model):

    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    amount = models.FloatField(default=0.0)
    payment_due = models.DateTimeField(auto_now_add=False)