from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


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

   courses = [
      {'courseName': 'Operating Systems', 'courseID':'COP4610', 'courseRating': 1.2},
      {'courseName': 'Data Structures II', 'courseID':'COP4530', 'courseRating': 4.8}
   ]


   context = {'courses': courses, 'username': userName}
   return render(request, 'schedulepage.html', context)

###############################################################################

"""
Renders page that shows advanced class ratings for premium users
If user is not a premium user, needs to redirect to schedule page again (NEED TO IMPLEMENT)
"""
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

###############################################################################

"""
Display the page that asks for input on what user to search for
When submitted, redirects to friendUserResults
"""
@login_required(login_url='/accounts/login')
def friendLookUp(request):
   return render(request, 'FriendLookUp.html', {})

###############################################################################

"""
Render the page to submit a review for a course
"""
@login_required(login_url='/accounts/login')
def addReview(request):

   if request.method == 'GET':
      return render(request, 'review.html', {})
   elif request.method == 'POST':

      # will need to do proper input validation
      examRating = request.POST['examRating']


      return render(request, 'review.html', {})
###############################################################################

"""
Recieve user to be rendered and display the list of usernames
If not accessed via post, redirect to home page 
"""
@login_required(login_url='/accounts/login')
def friendUserResults(request):
   if request.method == 'POST':

      # basic way to do this, need to research input validation and cleaning
      friendName = request.POST['friendUser']
      print(friendName)

      # will need to querey table to get rest of info once we get username

      context = {'friendName': friendName, 'userID': 'bmb22g', 'numClasses': 5}

      return render(request, 'friendResults.html', context)
   else:
      return render(request, 'home.html', {})

###############################################################################

"""
Check if user is logged in, then redirect to their respective schedule
Used after login auth to handle proper redirect
"""
def customRedirect(request):
   if request.user.is_authenticated:
      return redirect(f'/schedulepage/{request.user.username}')
   else:
      return redirect('/accounts/login')
   
###############################################################################
