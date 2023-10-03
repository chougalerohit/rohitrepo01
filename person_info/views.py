from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(r):
    return HttpResponse('<h1>Welcome to rohit second project,thanks for visit...! visit again</h1>')

def show(r):
    return HttpResponse('<h1>hi krish,thanks for visit...!  visit again...!</h1>')