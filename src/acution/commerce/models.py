
__author__ = 'naser'
from django.db import models
class User(models.Model):
    fullname = models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Good(models.Model):
    owner = models.ForeignKey(User)
    owner_price = models.ForeignKey(Price)
    city = models.CharField(max_length=20)
    comments = models.TextField()
    title = models.CharField(max_length=30)

class Price(models.Model):
    good = models.ForeignKey(Good)
    user = models.ForeignKey(User)
    amount = models.IntegerField()
    date = models.DateTimeField()

class Picture(models.Model):
    good = models.ForeignKey(Good)
    link = models.CharField(max_length=100)

class Notification(models.Model):
    good = models.ForeignKey(Good)
    user = models.ForeignKey(User)
    date_time = models.DateTimeField();