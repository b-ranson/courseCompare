from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advancedratings/<str:courseIDR>', views.advancedratings, name="advancedratings"),
    path('schedulepage/<str:userName>', views.schedulepage, name='schedulepage'),
    path('friendLookUp', views.friendLookUp, name='friendLookUp'),
    path('addReview', views.addReview, name='addReview'),
    path('friendUserResults', views.friendUserResults, name='friendUserResults'),
    path('addCourse', views.addCourse, name="addCourse"),
    path('paiduserupgrade', views.paiduserupgrade, name="paiduserupgrade"),
#    path('customRedirect', views.customRedirect, name='customRedirect'),
    path('accounts/registration', views.registration, name='registration'),
    path('accounts/login', views.userLogin, name='userLogin'),
    path('paiduserupgrade', views.paiduserupgrade, name='paiduserupgrade'),

    # Django Auth
#    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout")

]


# path('accounts/', include('django.contrib.auth.urls')),