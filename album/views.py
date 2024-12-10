from django.shortcuts import render, redirect

from album.models import Album  # Import redirect to handle post-redirect-get
from . import forms  # Import the form directly
from .forms import  AlbumForm
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
@method_decorator(login_required,name='dispatch') 
class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy("music")  # Correct URL for success
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to current user
        return super().form_valid(form)  # Call parent's form_valid method
