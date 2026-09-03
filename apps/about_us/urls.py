from django.urls import path
from .views import TeamView, life_at_mn_solutions

urlpatterns = [
    path('company/', TeamView.as_view(), name='about-us'),
    path('life-at-mn-solutions/', life_at_mn_solutions, name='life_at_mn_solutions'),
]