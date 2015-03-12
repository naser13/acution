from django.db import models
from django.contrib.auth.models import User


class Member(User):
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Good(models.Model):
    CATEGORIES = (
        ('car', 'خودرو'),
        ('elc', 'وسایل الکترونیکی'),
        ('hos', 'لوازم خانگی'),
    )

    owner = models.ForeignKey(Member)
    owner_price = models.IntegerField()
    city = models.CharField(max_length=20)
    comments = models.TextField()
    title = models.CharField(max_length=30)
    category = models.CharField(choices=CATEGORIES, max_length=3)

    def __str__(self):
        return self.title


class Price(models.Model):
    good = models.ForeignKey(Good)
    user = models.ForeignKey(Member)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount


class Picture(models.Model):
    good = models.ForeignKey(Good)
    # image = models.ImageField()


class Notification(models.Model):
    good = models.ForeignKey(Price)
    user = models.ForeignKey(Member)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_time