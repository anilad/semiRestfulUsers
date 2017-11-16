# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "usersApp/index.html", context)

def new(request):
    return render(request, "usersApp/new.html")

def create(request):
    result = User.objects.validate(request.POST)
    if len(result):
        for error in result:
            messages.info(request, error)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['fName'], last_name=request.POST['lName'], email=request.POST['email'])
        return redirect('/users')

def show(request, number):
    context = {
        "number": number,
        "user": User.objects.get(id=number)
    }
    return render(request, "usersApp/show.html", context)
def edit(request, number):
    context = {
        "number": number,
        "user": User.objects.get(id=number)
    }
    return render(request, "usersApp/edit.html", context)
def update(request, number):
    result = User.objects.validate(request.POST)
    print result
    if len(result):
        print "hi i'm in if"
        for error in result:
            messages.info(request, error)
            
        return redirect('/users/{number}/update')
    else:
        print "hi i'm in else"
        user=User.objects.get(id=number)
        user.first_name = request.POST['fName']
        user.last_name = request.POST['lName']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
def destroy(request, number):
    User.objects.get(id=number).delete()
    return redirect('/')