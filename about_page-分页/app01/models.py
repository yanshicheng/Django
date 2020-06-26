from django.db import models

# Create your models here.

class UserInfor(models.Model):
    username = models.CharField(max_length=24)
    addr = models.CharField(max_length=36)