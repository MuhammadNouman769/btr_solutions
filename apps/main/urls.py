from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact, name='contact_us'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blogs, name='blog'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('faqs/', views.faqs, name='faqs'),
    path('terms-conditions/', views.term_condition, name='term_condition'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('sqa/', views.sqa, name='sqa'),
]