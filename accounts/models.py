

#from django.contrib.auth.models import AbstractUser

#from django.utils.html import escape, make_safe

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this to avoid clashes
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change this to avoid clashes
        blank=True
    )

