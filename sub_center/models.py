# sub_center/models.py
from django.contrib.auth.models import User
from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subcenter_center')

    def __str__(self):
        return self.name
