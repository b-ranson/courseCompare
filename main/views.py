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
def advancedratings(request, className):

   #make db querey here based on className to pull advancedRatings
   # will hard code what table should look like for now

   # course name and ID, prof, section (this might be too tax to implement)
   # exam dif, hw dif, lecture dif, workload, total diff (all floats 0-5, prob averaged by integer inputs)

   #className gets passed in, then need to read db and pass vv this stuff
   # then need to pull advanced ratings from same class name and pass it


   courseOS = [
      {'courseName': 'Operating Systems', 'courseID':'COP4610', 'prof': 'Andy Wang', 'courseSection': '005'},
   ]
   advancedRatingsOS = [
      {'examDif': 2.3, 'hwDif': 3.7, 'lectDif': 2.8, 'workload': 4.8, 'avg': round((2.3 + 3.7 + 2.8 + 4.8)/5.0, 1)},
   ]

   courseDSII = [
      {'courseName': 'Data Structures II', 'courseID':'COP4530', 'prof': 'Bob Myers', 'courseSection': '002'},
   ]
   advancedRatingsDSII = [
      {'examDif': 4.6, 'hwDif': 2.8, 'lectDif': 3.3, 'workload': 4.1, 'avg': round((4.6 + 2.8 + 3.3 + 4.1)/5.0, 1)},
   ]


   context = {}
   if className == 'Operating Systems':
      context = { 'courses': courseOS, 'advRatings': advancedRatingsOS, 'className': className }
   elif className == 'Data Structures II':
      context = { 'courses': courseDSII, 'advRatings': advancedRatingsDSII, 'className': className }

   if className is not None:
      return render(request, 'advancedratings.html', context)
   else:
      return HttpResponse("Not Available")
      