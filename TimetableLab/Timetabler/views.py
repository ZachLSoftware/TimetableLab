from multiprocessing.context import _force_start_method
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory
from Timetabler.models import Availability
from Timetabler.models import Teacher
from Timetabler.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Timetabler.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

def index(request):
    return render(request, "index.html")

@login_required
def teachers(request):
    context={}
    teachers=Teacher.objects.filter(user=request.user)
    context['teachers']=teachers
    return render(request, "teachers.html", context)

def addTeacher(request, id=None):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        teacher = None
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        new_teacher=form.save(commit=False)
        new_teacher.user=request.user
        new_teacher.save()
        return redirect('teachers')
    return render(request, 'addTeacher.html',{'form': form})



def setAvailability(request, teacherid):
    context={}
    context['teacher']=Teacher.objects.get(id=teacherid)
    periods=['mon-1', 'tues-1', 'wed-1', 'thurs-1', 'fri-1', 
                     'mon-2', 'tues-2', 'wed-2', 'thurs-2', 'fri-2',
                     'mon-3', 'tues-3', 'wed-3', 'thurs-3', 'fri-3',
                     'mon-4', 'tues-4', 'wed-4', 'thurs-4', 'fri-4',
                     'mon-5', 'tues-5', 'wed-5', 'thurs-5', 'fri-5']
    availabilityFormSet = formset_factory(AvailabilityForm, extra=25)
    if request.method=='POST':
        formset1 = availabilityFormSet(request.POST, prefix='week1')
        if formset1.is_valid():
            i=0
            Availability.objects.filter(teacher=teacherid).filter(week=1).delete()
            for f in formset1:
                cd = f.cleaned_data
                period = cd.get('period')
                if(period):
                    newperiod=Availability()
                    newperiod.period=periods[i]
                    newperiod.week=1
                    newperiod.teacher=Teacher.objects.get(id=teacherid)
                    newperiod.save()
                i=i+1
        formset2 = availabilityFormSet(request.POST, prefix='week2')
        if formset2.is_valid():
            i=0
            Availability.objects.filter(teacher=teacherid).filter(week=2).delete()
            for f in formset2:
                cd = f.cleaned_data
                period = cd.get('period')
                if(period):
                    newperiod=Availability()
                    newperiod.period=periods[i]
                    newperiod.week=2
                    newperiod.teacher=Teacher.objects.get(id=teacherid)
                    newperiod.save()
                i=i+1
        return redirect(reverse('teachers'))
    else:
        formset1 = availabilityFormSet(prefix="week1")
        formset2 = availabilityFormSet(prefix="week2")
    
    currentQuery=Availability.objects.filter(teacher=teacherid).filter(week=1)
    current = []
    for c in currentQuery:
        current.append(periods.index(c.period)+1)
    currentQuery=Availability.objects.filter(teacher=teacherid).filter(week=2)
    for c in currentQuery:
        current.append(periods.index(c.period)+26)
    hours=Teacher.objects.values_list('totalHours', flat=True).get(id=teacherid)
    context['hours']=hours
    context['current']=current
    context['formset1']=formset1
    context['formset2']=formset2
    return render(request, 'availability.html', context)

def register(request):
    context={}
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http'
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            if email.send():
                username = form.cleaned_data.get('username')
                messages.success(request, f"Dear <b>{username}")
            else:
                message.error(request, f'Problem sending email')
            return redirect('index')
        else:
            context["form"] = form
    else:
        form = RegistrationForm()
        context['form']=form
    return render(request, 'registration/register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, "Activation Link is Invalid")
        return redirect('index')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')