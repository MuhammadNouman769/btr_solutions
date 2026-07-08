from django.urls import path
from .views import TeamView

urlpatterns = [
    path('company/', TeamView.as_view(), name='about-us'),
]