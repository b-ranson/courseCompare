from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
   return render(request, 'home.html', {})

#def login(request):
#   return render(request, 'login.html', {})

def schedulepage(request):
   username = request.user
   return render(request, 'schedulepage.html', {'name': username})

def advancedratings(request):
   return render(request, 'advancedratings.html', {})