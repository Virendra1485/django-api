from django.db import models

# Create your models here.


class StudentTbl(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    userid = models.CharField(max_length=50)
    password = models.CharField(max_length=30)