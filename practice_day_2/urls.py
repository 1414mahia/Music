"""
URL configuration for practice_day_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from musician import views 
from album import views 
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view', views.combined_view, name='view'),
    path('', views.combined_view_home, name='view_home'),
    path('album/', include("album.urls"),name='album'),  
    path('music/', include('musician.urls')),  
    path('view/', views.combined_view, name='view'),
    path('delete/<int:id>/', views.Delete.as_view(), name='delete_musician'),
    path('edit/<int:id>/', views.Edit.as_view(), name='edit_musician'),
]
