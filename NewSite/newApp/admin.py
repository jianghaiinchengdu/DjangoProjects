# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


class customerAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'email')

    search_fields = ('last_name',)
    list_per_page = 2

class modelAdmin(admin.ModelAdmin):
    list_display = ('param1','param2','param3','param4')

admin.site.register(Author,customerAdmin)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(TestModel,modelAdmin)