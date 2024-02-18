from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'home.html', {})

@login_required(login_url='/accounts/login')
def schedulepage(request):
   # db logic here, or mode to model functions? need to look into more
   # will hard code for right now to update template with jinja syntax

   courses = [
      {'courseName': 'Operating Systems', 'courseID':'COP4610', 'courseRating': 1.2},
      {'courseName': 'Data Structures II', 'courseID':'COP4530', 'courseRating': 4.8}
   ]

   context = {'courses': courses}
   return render(request, 'schedulepage.html', context)

@login_required(login_url='/accounts/login')
def advancedratings(request):



   return render(request, 'advancedratings.html', {})