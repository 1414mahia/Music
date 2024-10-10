from django.shortcuts import render, redirect  # Add redirect to handle post-redirect-get
from . import forms  # Import the form directly
from .models import MusicModel

# Create your views here.
def music(request):
    if request.method == 'POST':
        add_music = forms.MusicianForm(request.POST)
        if add_music.is_valid():  # Call is_valid() as a method
            add_music.save()
            return redirect('album')  # Redirect to the music home or another view after saving
    else:
        add_music = forms.MusicianForm()
        
    return render(request, 'music.html', {'form': add_music})
