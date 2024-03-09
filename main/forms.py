from django import forms

class CourseReviewForm(forms.Form):
    examRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    homeworkRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    lectureRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)
    workloadRating = forms.DecimalField(min_value=0, max_value=5, max_digits=1, decimal_places=0)

    def getCleanInput(self):
        examRating = self.cleaned_data.get('examRating')
        homeworkRating = self.cleaned_data.get('homeworkRating')    
        lectureRating = self.cleaned_data.get('lectureRating')    
        workloadRating = self.cleaned_data.get('workloadRating')    
    
        return ((examRating, homeworkRating, lectureRating, workloadRating))
class FriendLookUpForm(forms.Form):
    friendUser = forms.CharField(max_length=50, required=True)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())
    firstName = forms.CharField(max_length=50, required=True)
    lastName = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput())

    def getCleanInput(self):
        username = self.cleaned_data.get('username').upper()
        password = self.cleaned_data.get('password')
        firstName = self.cleaned_data.get('firstName').upper()
        lastName = self.cleaned_data.get('lastName').upper()
        email = self.cleaned_data.get('email').upper()

        return((username, password, firstName, lastName, email))
    
    def emailCheck(self):
        email = self.cleaned_data.get('email').upper()

        username, domain = email.split('@')
        if domain == 'FSU.EDU':
            return True
        else:
            return False
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())

    def getCleanInput(self):
        username = self.cleaned_data.get('username').upper()
        password = self.cleaned_data.get('password')

        return ((username, password))