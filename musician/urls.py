from django.urls import path
from .import views
urlpatterns = [
    path('',views.Musician.as_view() ,name='music'),
    path('register/',views.Register,name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

]
