from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jewel(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=32, unique=True)
    category = models.ForeignKey('Category', blank=True)
    rating = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
    image = models.ImageField(upload_to='img', blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    def __str__(self):
        return self.image.url

class Category(models.Model):
    name = models.CharField(verbose_name=u'название', max_length=16, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    def __str__(self):
        return self.name

