#!/usr/bin/env python
# encoding utf-8

from django.http import HttpResponse
from django.template import *
from django.shortcuts import render_to_response
from newApp.models import Author
import sqlite3
import datetime
import WSG


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self):
        return "helllllllllo"
    sayhello.alerts_data = True

def hello(request):
    res = []
    a = WSG
    return HttpResponse(Author.objects.all()[0].email)
    # person = Person('jiangha111', i)
    # res.append(person)
    a = sqlite3.connect('../db.sqlite3')
    cursor = a.cursor()
    # cursor.execute("CREATE TABLE Person (name text,age integer,address text)")

    # for j in range(0, 10):
    #     cursor.execute("INSERT INTO Person VALUES ('jianghai%d',%d,'sss')" % (j,j))
    #     res.append(cursor.fetchall())
    cursor.execute("DROP TABLE newApp_testmodel")
    des = cursor.fetchall()
    print(des)

    a.close()
    return render_to_response('HomePage.html', {'personList': res})


def getName(request):
    now = datetime.datetime.now()
    html = "<html><body><input type='button' value='It is now %s.' width='100px'></input></body></html>" % now
    return HttpResponse(html)
