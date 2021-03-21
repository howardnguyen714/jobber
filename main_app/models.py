from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    speaker = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=200)

    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
    