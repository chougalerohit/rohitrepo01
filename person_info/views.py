from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(r):
    return HttpResponse('<h1>Welcome to rohit second project</h1>')

def show(r):
    return HttpResponse('<h1>Hi krishnat how r you,i think u r doing well right</h1>')