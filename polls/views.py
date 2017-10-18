from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hey world, this is the polls index')

def cheeseburger(request):
    return HttpResponse('Here is a cheeseburger')