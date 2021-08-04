from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    bio= models.CharField(max_length=140)
    joined_date = models.DateField(auto_now_add=True)
    follows = models.ManyToManyField("self", symmetrical=False)
# Create your models here.
