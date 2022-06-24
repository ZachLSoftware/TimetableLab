from django import forms

from .models import Teacher
  
# create a form
class AvailabilityForm(forms.Form):
    period = forms.BooleanField()



class TeacherForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['id'].required=False
    class Meta:
        model = Teacher
        fields = ('name', 'totalHours', 'id',)
        widgets = {'id': forms.HiddenInput()}