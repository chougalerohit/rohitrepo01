from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(r):
    return HttpResponse('<h1>Hi,welcome to rohit second project</h1>')

def show(r):
    return HttpResponse('<h1>hi krishna....!! how r u...?</h1>')