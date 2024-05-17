from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
import random, os, json
import random
import string
import uuid
from .forms import DocumentForm 
from .models import Document, Board



@login_required

def home(request):
    user_documents = Document.objects.filter(user=request.user)
    user_boards = Board.objects.filter(user=request.user)
    return render(request, "home.html", {"user_documents": user_documents, "user_boards": user_boards})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    

@require_POST
def custom_logout(request):
    auth_logout(request)
    return redirect('login')

def archive(request):
    return render(request, "archive.html")

def document(request):
    return render(request, "document.html")

def doc(request):
    return render(request, "doc.html")

def document_js(request):
    js_file_path = finders.find('document.js')
    if js_file_path:
        with open(js_file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='text/javascript')
    else:
        return HttpResponse(status=404)
    
def doc_js(request):
    js_file_path = finders.find('doc.js')
    if js_file_path:
        with open(js_file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='text/javascript')
    else:
        return HttpResponse(status=404)
    
@csrf_exempt
def update_title(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_title = data.get('title')
        if new_title:
            document = Document.objects.first()
            document.title = new_title
            document.save()
            return JsonResponse({'message': 'Title updated successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image_path = settings.MEDIA_URL + uploaded_image.name
        document = Document.objects.create(image=image_path)
        absolute_image_url = request.build_absolute_uri(document.image.url)
        
        return JsonResponse({'success': True, 'image_path': absolute_image_url})
    else:
        return JsonResponse({'success': False, 'message': 'No image uploaded or invalid request'})

def share_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    shareable_link = generate_shareable_link() 
    document.shareable_link = shareable_link
    document.save()
    
    return JsonResponse({'shareable_link': shareable_link})


def generate_shareable_link():
    return str(uuid.uuid4())


def share_via_link(request, document_id):
    document = Document.objects.get(id=document_id)
    return render(request, 'doc.html', {'document': document})


def newdoc(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user  
            document.save()
            return redirect('document') 
    else:
        form = DocumentForm()
    return render(request, 'newdoc.html', {'form': form})

@login_required
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            document = Document.objects.create(user=request.user, title=title, content=content)
            return redirect('home')
    return render(request, 'create_document.html')

@login_required
def create_board(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            board = Board.objects.create(user=request.user, title=title)
            return redirect('home')
    return render(request, 'create_board.html')

def about(request):
    return render(request, "about.html")


