#!/usr/bin/env python
from django.http import HttpResponse
from django.template import *
from django.shortcuts import render_to_response
import sqlite3
import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self):
        return "helllllllllo"
    sayhello.alerts_data = True

def hello(request):
    res = []
    for i in range(1, 20):
        person = Person('jiangha111', i)
        res.append(person)
        a = sqlite3.connect('../db.sqlite3')
        # a.execute('CREATE TABLE Persons(Id_P int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))')
        # print(a)
        a.execute("INSERT INTO Persons('sss','jianghai','sss','asdfsdf','ssssssss')")
    return render_to_response('HomePage.html', {'personList': res})


def getName(request):
    now = datetime.datetime.now()
    html = "<html><body><input type='button' value='It is now %s.' width='100px'></input></body></html>" % now
    return HttpResponse(html)
