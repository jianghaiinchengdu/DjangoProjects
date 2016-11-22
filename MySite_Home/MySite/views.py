# encoding:utf-8
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
import re

def entry(request):
    path = request.path

   # return HttpResponse(json.dumps(
      #  {'name':'ss',
      #   'age':10,
     #    'arr':
     #        ["jiang",'hai']
     #    }
   # ), content_type = "application/json")
    # return HttpResponse(json({'name':'ss'}))

    aboutPattern = re.compile(r'^index$')
    homePattern = re.compile(r'^home$')
    servicePattern = re.compile(r'^service$')
    productsPattern = re.compile(r'^products$')
    contactPattern = re.compile(r'^contact$')

    if (path.find('home.html') != -1):
        return render_to_response('home.html')
    if (path.find('aboutus.html') != -1):
            return render_to_response('aboutus.html')
    if (path.find('service.html') != -1):
            return render_to_response('service.html')
    if (path.find('products.html') != -1):
            return render_to_response('products.html')
    if (path.find('contact.html') != -1):
            return render_to_response('contact.html')
    if (path.find('play.html') != -1):
            return render_to_response('play.html')
    return render_to_response('home.html')


