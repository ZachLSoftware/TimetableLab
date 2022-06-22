from django import forms
  
# create a form
class AvailabilityForm(forms.Form):
    day = forms.BooleanField()