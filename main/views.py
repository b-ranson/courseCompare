from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import *
from django.db.models import Count
from django.db.models import Q

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
@allowed_user(allowed_roles = ['PAIDUSER'])
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

      allCourses = Courses.objects.all()
   
      # hardcoding for now, josh add query for prefixes here then pass in, key word is prefixes for html template
      # passing in empty one first makes it look better on template fyi
      return render(request, 'review/review.html', {"prefixes": ["   ", "COP", "CEN", "MAC"]})
   
   elif request.method == 'POST':      

      form = forms.CourseReviewForm(request.POST)
      print(form)
      if form.is_valid():
         examRating, homeworkRating, lectureRating, workloadRating, coursePrefix, courseNumber = form.getCleanInput()

      # do check of prefix and number here and get courseID, then use it below. commenting out for now
      # so nothing gets messed up while courseID is not being found 

      """
      Course = Courses.objects.get(courseID = courseID)
      Course.numOfRatings = Course.numOfRatings + 1
      Course.examDiff = (Course.examDiff * Course.numOfRatings + examRating)/Course.numOfRating
      Course.lectureDiff = (Course.lectureDiff * Course.numOfRatings + lectureRating)/Course.numOfRating
      Course.workLoad = (Course.workLoad * Course.numOfRatings + workloadRating)/Course.numOfRating
      Course.homeworkDiff = (Course.homeworkDiff * Course.numOfRatings + homeworkRating)/Course.numOfRating
      Course.save()
      """
      return redirect('/addReview')
###############################################################################

"""
Recieve user to be rendered and display the list of usernames
If not accessed via post, redirect to home page
"""
@login_required(login_url='/accounts/login')
def friendUserResults(request):
   if request.method == 'POST':

      form = forms.FriendLookUpForm(request.POST)
      print(form)
      if form.is_valid():
         friendUserName = form.cleaned_data['friendUser']
         friend = models.MyCustomUser.objects.get(username = friendUserName)

         numClasses = CourseTaking.objects.filter(username = friend.username).count()

      context = {'friendName': friend.username, 'userID': friend.id, 'numClasses': numClasses}

      return render(request, 'userLookup/friendResults.html', context)

   else:
      return render(request, 'home.html', {})

###############################################################################

"""
Page where users can view and add courses to their schedule on their account
"""
@login_required(login_url='/accounts/login')
def addCourse(request):

   if request.method == 'GET':
      return render(request, 'addCourse/searchCourse.html')
   elif request.method == 'POST':

      form = forms.addCourseForm(request.POST)
      if form.is_valid():

         coursePrefix, courseNumber = form.getCleanInput()

         coursePrefix.upper()

         allCourses = Courses.objects.all().filter(Q(courseLetters = coursePrefix) | Q(courseNumber = courseNumber))
         course = []
         for x in allCourses:
            course.append({'courseName': x.courseName,'courseID':x.courseID,'courseRating': round((x.homeworkDiff+x.lectureDiff+x.workLoad+x.examDiff)/4)})
         contex = {'courses':course}
         return render(request, 'addCourse/addCourse_schedule.html', contex)
      else:
         return render(request, 'home.html')

###############################################################################
      
@login_required(login_url='/accounts/login')
def addCourseToSchedule(request):
   if request.method == 'POST':
      set = CourseTaking.objects.all().filter(username = request.user.username, courseID = request.POST['courseID'])
      if not set:
         CourseTaking.objects.create(username = request.user.username, courseID = request.POST['courseID'])
      return redirect(f'/schedulepage/{request.user.username}')
   
###############################################################################
   
@login_required(login_url='/accounts/login')
def deleteCourseFromSch(request):
   if request.method == 'POST':
      delObject = CourseTaking.objects.get(username = request.user.username, courseID = request.POST['courseID'])
      delObject.delete()
      return redirect(f'/schedulepage/{request.user.username}')


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


###############################################################################

@login_required(login_url='/accounts/login')
def paiduserupgrade(request):
   group = Group.objects.get(name="PAIDUSER")
   request.user.groups.add(group)
   return redirect(f'/schedulepage/{request.user.username}')

###############################################################################

def forgotPassword(request):
   
   if request.method == 'GET':
      return render(request, 'accounts/forgotPass.html')
   elif request.method == 'POST':
      
      form = forms.forgotPasswordForm(request.POST)
      
      if form.is_valid():
         username, email, newPassword, confirmPassword = form.getCleanInput()

         

      return redirect('/accounts/login')