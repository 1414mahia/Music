from django import forms
from .models import MusicModel  # Use the correct import statement
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = '__all__'  # This will include all fields from the MusicModel
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id' :'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id' :'required'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']