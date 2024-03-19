from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import *

from . import forms
from . import models

###############################################################################

"""
Renders the home page where users can go to the login page
"""
def home(request):
   return render(request, 'home.html', {})

###############################################################################

"""
Renders the schedule page for all users
This is the "home" page after login and where the user should always end up
"""
@login_required(login_url='/accounts/login')
def schedulepage(request, userName):
   # db logic here, or mode to model functions? need to look into more
   # will hard code for right now to update template with jinja syntax

   # need to do querey based on userName

   cTaking = CourseTaking.objects.all().filter(username = userName)

   courses = []

   for x in cTaking:
      course = Courses.objects.get(courseID = x.courseID)
      courses.append({'courseID': course.courseLetters + str(course.courseNumber),'courseName': course.courseName,'courseRating':round((course.homeworkDiff+course.lectureDiff+course.workLoad+course.examDiff)/4),'courseIncID':course.courseID})

   context = {'courses': courses, 'username': userName}
   return render(request, 'scheduleAndRatings/schedulepage.html', context)

###############################################################################

"""
Renders page that shows advanced class ratings for premium users
If user is not a premium user, needs to redirect to schedule page again (NEED TO IMPLEMENT)
"""
@login_required(login_url='/accounts/login')
def advancedratings(request,courseIDR):

   # make db querey here based on courseID parameter to pull advancedRating
   course = Courses.objects.get(courseID = courseIDR)
   courseData = {'courseName': course.courseName, 'courseID':course.courseLetters + str(course.courseNumber), 'prof': course.professor, 'courseSection': '002'}
   advRating = {'examDif': course.examDiff, 'hwDif':course.homeworkDiff, 'lectDif': course.lectureDiff, 'workload': course.workLoad, 'avg': round((course.homeworkDiff+course.lectureDiff+course.workLoad+course.examDiff)/4),'courseIncID':course.courseID}
   context = {'courses': courseData, 'advRatings': advRating, 'className': course.courseName}


   if courseIDR is not None:
      return render(request, 'scheduleAndRatings/advancedratings.html', context)
   else:
      return HttpResponse("Not Available")

###############################################################################

"""
Display the page that asks for input on what user to search for
When submitted, redirects to friendUserResults
"""
@login_required(login_url='/accounts/login')
def friendLookUp(request):
   return render(request, 'userLookup/FriendLookUp.html', {})

###############################################################################

"""
Render the page to submit a review for a course
"""
@login_required(login_url='/accounts/login')
def addReview(request):

   if request.method == 'GET':

      # here need query of all available classes to rate and then pass into the html file (josh)
      # have selection as a drop down (aiden)

      return render(request, 'review/review.html', {})
   elif request.method == 'POST':

      # josh all for you for queries to add new averages into db for respective class
      # (lmk when the course selection stuff is added and ill add it to the form method)
      form = forms.CourseReviewForm(request.POST)
      if form.is_valid():
         examRating, homeworkRating, lectureRating, workloadRating = form.getCleanInput()

      return render(request, 'review/review.html', {})
###############################################################################

"""
Recieve user to be rendered and display the list of usernames
If not accessed via post, redirect to home page 
"""
@login_required(login_url='/accounts/login')
def friendUserResults(request):
   if request.method == 'POST':

      form = forms.FriendLookUpForm(request.POST)
      if form.is_valid():
         friendName = form.cleaned_data['friendUser']
         print(friendName)

      # will need to query table to get rest of info once we get username
      # hard coding for now
      # if there is a way to make sql query a dict like this, would make implementing very easy
      # still need to pass context as dict for html templatex
      context = {'friendName': friendName, 'userID': 'bmb22g', 'numClasses': 5}

      return render(request, 'userLookup/friendResults.html', context)
   
   else:
      return render(request, 'home.html', {})

###############################################################################

@login_required(login_url='/accounts/login')
def addCourse(request):
   return render(request, 'home.html', {})

###############################################################################

"""
Registration page for users to create account. Defaults to basic, nonstaff
and non sudo account. Also confirms that email is an fsu email
"""
def registration(request):
   if request.method == 'GET':
      return render(request, 'accounts/registration.html', {})
   elif request.method == 'POST':

      form = forms.RegistrationForm(request.POST)
      if form.is_valid():
         username, password, firstName, lastName, email = form.getCleanInput()
         if not form.emailCheck():
            return HttpResponse("Must use FSU email to create account.")
         user = models.MyCustomUser.objects.create_user(email=email, 
                                                        password=password,
                                                        username=username,
                                                        first_name=firstName,
                                                        last_name=lastName,
                                                        is_superuser=False,
                                                        is_active=True,
                                                        is_staff=False,
                                                        date_joined=timezone.now(),
                                                        last_login=None)
         
         return redirect('/accounts/login')
      else:
         return redirect('/accounts/registration')

###############################################################################

"""
Login function 
"""
def userLogin(request):
   if request.method == 'GET':
      return render(request, 'accounts/login.html', {})

   elif request.method == 'POST':

      form = forms.LoginForm(request.POST)
      if form.is_valid():
         username, password = form.getCleanInput()
         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            return redirect(f'/schedulepage/{request.user.username}')         
         else:
            return HttpResponse("Incorrect Username or Password")
      else:
         return HttpResponse("Incorrect Username or Password")