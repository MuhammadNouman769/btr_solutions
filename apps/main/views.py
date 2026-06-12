from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')

def projects(request):
    return render(request, 'main/projects.html')

def signin(request):
    return render(request, 'main/signin.html')

def signup(request):
    return render(request, 'main/signup.html')

def blog_single(request):
    return render(request, 'main/blog-single.html')