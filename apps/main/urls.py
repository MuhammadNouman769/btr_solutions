from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact_us'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blogs, name='blog'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('case-studies/', views.case_studies, name='case_studies'),
]