from djongo import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uid = models.BigAutoField(primary_key=True)
    sub = models.CharField(max_length=500, unique=True) 
    email = models.EmailField(max_length=255)
    # ArrayList of questions(fk) (onetomany) --Dont add this
    name = models.CharField(max_length=255, null=True, default="")
    year_of_study = models.PositiveIntegerField(null=True, default=1)
    prn = models.IntegerField(null=True, unique=True)

    # USERNAME_FIELD = 'sub'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.sub
    

