from django.shortcuts import render, redirect  # Import redirect to handle post-redirect-get
from . import forms  # Import the form directly

# Create your views here.
def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)  # Use request.POST with uppercase 'POST'
        if album_form.is_valid():  # Call is_valid() as a method
            album_form.save()
            return redirect('view')  # Redirect to the album page or another view after saving
    else:
        album_form = forms.AlbumForm()

    return render(request, 'album.html', {'form': album_form})
