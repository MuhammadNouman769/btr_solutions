from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('blog-single/', views.blog_single, name='blog_single'),
]