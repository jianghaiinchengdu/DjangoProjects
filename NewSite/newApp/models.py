# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True,null=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(verbose_name='contact Way')

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self.email

    def __str__(self):
        return u'%s %s %s' % (self.first_name, self.last_name,self.email)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()


class TestModel(models.Model):
    param1 = models.CharField(max_length=100, blank=True, null=True)
    param2 = models.CharField(max_length=100, blank=True)
    param4 = models.CharField(max_length=100, blank=True)
    param3 = models.DateTimeField('sss',auto_now=True)
