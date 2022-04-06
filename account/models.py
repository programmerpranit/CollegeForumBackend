from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uid = models.BigAutoField(primary_key=True)
    sub = models.CharField(max_length=500, unique=True) 
    useremail = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, default="")
    year_of_study = models.PositiveIntegerField(null=True, default=1)
    prn = models.IntegerField(null=True, unique=True)

    REQUIRED_FIELDS = []


    def __str__(self):
        return self.sub
    

