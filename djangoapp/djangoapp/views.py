from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about Page')


def home(request):
    return render(request, 'home.html')
