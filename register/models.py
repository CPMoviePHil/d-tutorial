from django.db import models


# Create your models here.
class Members(models.Model):
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)


class Profile(models.Model):
    profile = models.ForeignKey(Members, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField(default=1)
    birthday = models.DateTimeField()

