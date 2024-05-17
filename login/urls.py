from django.contrib.auth import views as auth_views
#from .views import update_title
#from .views import upload_image
from django.urls import path
from . import views
from .views import newdoc

urlpatterns = [
    path('', views.home, name='home'),  # Uncomment if you want to use the home page
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    #path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('archive/', views.archive, name='archive'),
    path('document/', views.document, name='document'),
    path('doc/', views.doc, name='doc'),
    path('document.js', views.document_js, name='document_js'),
    #path('doc.js', views.doc_js, name='doc_js'),
    path('update_title/', views.update_title, name='update_title'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('shared/<int:document_id>/', views.share_via_link, name='shared_document'),
    path('create/', views.newdoc, name='newdoc'),
    path('create_document/', views.create_document, name='create_document'),
    path('create_board/', views.create_board, name='create_board'),
    path('about/', views.about, name='about'),
]

