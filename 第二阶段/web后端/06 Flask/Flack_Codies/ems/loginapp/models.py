from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    headpic=models.ImageField(upload_to="pics")


class Test(models.Model):
    name=models.CharField(max_length=20)
    age=models.SmallIntegerField()
    salary=models.DecimalField(max_digits=7,decimal_places=2)
    headpic=models.ImageField(upload_to="pics")
