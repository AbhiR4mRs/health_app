from django.contrib.auth.models import User
from django.db import models

class Center(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_centers')  # HQ
    # created_at, contact_number, etc. (optional)
