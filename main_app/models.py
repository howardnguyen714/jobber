from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your models here.
=======
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateField('Date User Joined')
>>>>>>> submain
