from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Travel
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all(),
        # 'travel' : Travel.objects.all()
    }
    return render(request, 'trips/index.html', context)

def register(request):
     errors = User.objects.validator(request.POST)
     if 'err_messages' in errors:
        for error in errors['err_messages']:
            messages.error(request, error)
        return redirect('/')
     else: 
        return redirect('/travels')

def login(request):
    print session
    return render(request, '/travels')

def travels(request):
    context = {
        'trips': Travel.objects.all()
    }
    return render(request, 'trips/travels.html', context)

def logout(request):
    return redirect('/')

def create(request):
    errors = User.objects.validator(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Travel.objects.create(
            destination=request.POST['destination'],
            desc=request.POST['desc']
        )
    return redirect('/travel')

    Travel.objects.create(
        destination=request.POST['destination'],
        desc=request.POST['desc'],
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date'],
    )
    return redirect('/travels')

