from django.shortcuts import render,redirect,get_object_or_404
import musician
from musician.forms import MusicianForm
from musician.models import MusicModel  # Import specific model
from album.models import Album  
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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

def combined_view_home(request):
    albums = Album.objects.all()  # Fetch all albums
    musicians = MusicModel.objects.all()  # Fetch all musicians

    context = {
        'albums': albums,
        'musicians': musicians,
    }
    return render(request, 'home_page_view.html', context)

@method_decorator(login_required,name='dispatch') 
class Delete(DeleteView):
    model =MusicModel
    
    template_name='delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("view")

@method_decorator(login_required,name='dispatch') 
class Edit(UpdateView):
    model =MusicModel
    form_class =MusicianForm
    template_name='music.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("view")
