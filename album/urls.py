from django.urls import path
from .import views
urlpatterns = [
    path('',views.AddAlbum.as_view() ,name='album')
]
