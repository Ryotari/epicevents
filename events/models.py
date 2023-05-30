from django.db import models
from users.models import Client
from django.contrib.auth.models import User

class Event(models.Model):

    EVENT_STATUS = [
        ('CREATED', 'created'),
        ('INPROGRESS', 'in_progress'),
        ('FINISHED', 'finished')
    ]
    name = models.CharField(max_length=30, null=True, blank=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    event_status = models.CharField(max_length=20, choices=EVENT_STATUS)

    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField(auto_now_add=False)

    notes = models.TextField(null=True, blank=True)
