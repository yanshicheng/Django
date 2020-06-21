from django.db import models

# Create your models here.

GENDER_CHOICES = ((0,'男'),(1,'女'))

class UserInfo(models.Model):
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=24)
    phone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True)
    gender = models.PositiveIntegerField(choices=GENDER_CHOICES,default=0)
    def __str__(self):
        return self.username
