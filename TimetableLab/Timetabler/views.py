from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory
from Timetabler.models import Availability
from Timetabler.models import Teacher
from Timetabler.forms import *

def index(request):
    return render(request, "index.html")

def teachers(request):
    context={}
    teachers=Teacher.objects.all()
    context['teachers']=teachers
    return render(request, "teachers.html", context)

def addTeacher(request, id=None):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        teacher = None
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teachers')
    return render(request, 'addTeacher.html',{'form': form})



def setAvailability(request, teacherid):
    context={}
    context['teacher']=teacherid
    periods=['mon-1', 'tues-1', 'wed-1', 'thurs-1', 'fri-1', 
                     'mon-2', 'tues-2', 'wed-2', 'thurs-2', 'fri-2',
                     'mon-3', 'tues-3', 'wed-3', 'thurs-3', 'fri-3',
                     'mon-4', 'tues-4', 'wed-4', 'thurs-4', 'fri-4',
                     'mon-5', 'tues-5', 'wed-5', 'thurs-5', 'fri-5']
    availabilityFormSet = formset_factory(AvailabilityForm, extra=25)
    if request.method=='POST':
        formset = availabilityFormSet(request.POST)
        if formset.is_valid():
            i=0
            Availability.objects.filter(teacher=teacherid).delete()
            for f in formset:
                cd = f.cleaned_data
                period = cd.get('period')
                if(period):
                    newperiod=Availability()
                    newperiod.period=periods[i]
                    newperiod.teacher=Teacher.objects.get(id=teacherid)
                    newperiod.save()
                i=i+1
            return redirect(reverse('index'))
    else:
        formset = availabilityFormSet()
    
    currentQuery=Availability.objects.filter(teacher=teacherid)
    current = []
    for c in currentQuery:
        current.append(periods.index(c.period)+1)
    context['current']=current
    context['formset']=formset
    return render(request, 'availability.html', context)