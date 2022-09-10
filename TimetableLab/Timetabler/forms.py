from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher, User
from django.contrib.auth import get_user_model
from django.forms import ValidationError

class RegistrationForm(UserCreationForm):
    #username = forms.CharField(label='username', min_length=5, max_length=30)
    #email=forms.EmailField(label="email")
    #password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    #password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
    class Meta:
        model = get_user_model()
        fields = ("username", "email", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = """
            <ul>
                <li id="charLength">Your password must contain at least 8 characters.</li>
                <li id="numCheck">Your password can’t be entirely numeric.</li>
            </ul>"""

# create a form
class AvailabilityForm(forms.Form):
    period = forms.BooleanField()

class ModuleForm(forms.Form):
    moduleName = forms.CharField()

class TeacherForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['id'].required=False
    class Meta:
        model = Teacher
        fields = ('name', 'totalHours', 'id',)
        widgets = {'id': forms.HiddenInput()}