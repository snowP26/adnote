from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Uncomment if you want to use the home page
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('login/', views.login_view, name='login'),  # Updated to login_view
    path('home/', views.home, name='home'),
]

