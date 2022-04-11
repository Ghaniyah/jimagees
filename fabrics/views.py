from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this is my first django project

def index(response):
    return HttpResponse("<h1>jimagees fabrics</h1>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")
