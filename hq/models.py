from django.db import models
from django.contrib.auth.models import User, Group

class PublicContent(models.Model):
    CONTENT_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('file', 'File'),
    ]

    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    text_content = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Center(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_subcenter = models.BooleanField(default=False)
    parent_center = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'is_subcenter': False})
    
    def __str__(self):
        return self.name