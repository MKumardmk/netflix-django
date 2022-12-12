from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email or phone number'}))
    password= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model=Profile
        exclude=['uuid']
        fields= ['name','password']
        