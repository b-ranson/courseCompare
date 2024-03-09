from django import forms

class CourseReviewForm(forms.Form):
    examRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    homeworkRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    lectureRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    workloadRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    
class FriendLookUpForm(forms.Form):
    friendUser = forms.CharField(max_length=50, required=True)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())
    firstName = forms.CharField(max_length=50, required=True)
    lastName = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())