from django import forms
from .models import MusicModel  # Use the correct import statement

class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = '__all__'  # This will include all fields from the MusicModel
