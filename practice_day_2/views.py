from django.shortcuts import render,redirect,get_object_or_404
import musician
from musician.forms import MusicianForm
from musician.models import MusicModel  # Import specific model
from album.models import Album  

def home(request):
    return render(request, 'home.html')

def combined_view(request):
    albums = Album.objects.all()  # Fetch all albums
    musicians = MusicModel.objects.all()  # Fetch all musicians

    context = {
        'albums': albums,
        'musicians': musicians,
    }
    return render(request, 'view.html', context)

def delete(request,id):
    musician = get_object_or_404(MusicModel, id=id)
    musician.albums.all().delete()
    musician.delete()
    return render(request, 'home.html', {}) 


def edit(request, id):
 musician = get_object_or_404(MusicModel, id=id)
 # Fetch the musician to edit

 if request.method == 'POST':
        form= MusicianForm(request.POST, instance=musician)  # Bind form with musician instance
        if form.is_valid():
            form.save()  # Save the updated musician details
            return redirect('view')  # Redirect after saving
 else:
        form = MusicianForm(instance=musician)  # Show current data in the form

 return render(request, 'music.html', {'form': form, 'musician': musician})