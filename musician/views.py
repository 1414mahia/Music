from django.shortcuts import render, redirect  # Add redirect to handle post-redirect-get
from . import forms  # Import the form directly
from .models import MusicModel
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import logout
from  .forms import MusicianForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView

@method_decorator(login_required,name='dispatch') #dispatch hocche unloged user access korte parbe nh
class Musician(CreateView):
    model = MusicModel
    form_class = MusicianForm
    template_name = 'music.html'
    success_url = reverse_lazy("music")  # Correct URL for success
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to current user
        return super().form_valid(form)  # Call parent's form_valid method
    
def Register(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)  # Fixed typo
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Registration is successful')  # Fixed spelling
            return redirect("login")
    else:
        registration_form = RegistrationForm()  # Fixed typo

    return render(request, 'register.html', {'form': registration_form})

class UserLoginView(LoginView):
    template_name='register.html'
    def get_success_url(self):
        return reverse_lazy("view")
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
def user_logout(request):
    logout(request)
    return redirect("login")