from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')

def contact(request):
    return render(request, 'home/contact-us.html')

def services(request):
    return render(request, 'home/services.html')

def projects(request):
    return render(request, 'home/projects.html')

def signin(request):
    return render(request, 'home/signin.html')

def signup(request):
    return render(request, 'home/signup.html')

def blogs(request):
    return render(request, 'blogs/blog-grid.html')

def blog_single(request):
    return render(request, 'home/blog-single.html')

def case_studies(request):
    return render(request, 'home/case-studies.html')

def faqs(request):
    return render(request, 'faqs/faqs.html')