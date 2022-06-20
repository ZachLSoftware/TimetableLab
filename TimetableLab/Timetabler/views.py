from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def teachers(request):
    return render(request, "teachers.html")