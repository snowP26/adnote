from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in authentication URLs
]
