from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'home.html', {})

@login_required(login_url='/accounts/login')
def schedulepage(request):
   return render(request, 'schedulepage.html', {})

@login_required(login_url='/accounts/login')
def advancedratings(request):
   return render(request, 'advancedratings.html', {})