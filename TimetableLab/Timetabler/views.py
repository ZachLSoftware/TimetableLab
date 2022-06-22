from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.forms import formset_factory
from Timetabler.forms import AvailabilityForm

def index(request):
    return render(request, "index.html")

def teachers(request):
    return render(request, "teachers.html")

def setAvailability(request):
    availabilityFormSet = formset_factory(AvailabilityForm, extra=25)
    if request.method=='POST':
        formset = availabilityFormSet(request.POST)
        if formset.is_valid():
            for f in formset:
                cd = f.cleaned_data
                day = cd.get('day')
            return redirect(reverse('index'))
    else:      
        formset = availabilityFormSet()
    return render(request, 'availability.html', {'formset':formset})