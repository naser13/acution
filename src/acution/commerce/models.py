from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from acution.commerce.data import Data


class Member(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.first_name + " " + self.last_name

class Good(models.Model):
    CATEGORIES = (
        ('cth', 'پوشاک'),
        ('elc', 'وسایل الکترونیکی'),
        ('hos', 'لوازم خانگی'),
    )
    owner = models.ForeignKey(Member)
    owner_price = models.IntegerField(verbose_name='قیمت اولیه')
    city = models.CharField(max_length=20, verbose_name='شهر')
    description = models.TextField(verbose_name='توضیحات')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    category = models.CharField(choices=CATEGORIES, max_length=3, verbose_name='دسته بندی')

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
    image = models.FileField(upload_to=settings.MEDIA_ROOT)


class Notification(models.Model):
    good = models.ForeignKey(Price)
    user = models.ForeignKey(Member)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_time