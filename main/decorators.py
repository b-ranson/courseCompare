from django.http import HttpResponse
from django.shortcuts import redirect

def unauthed_user(view_func): #this is used to keep users that are not logged only able to get to sign up and login page
    #use a @unauthed_user to make a page like this
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            redirect('/accounts/login') #this should show the login page
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def dec(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = ""
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page')
        return wrapper_func
    return dec

#when used, use @allowed_user(allowed_roles = ['name of roles'])