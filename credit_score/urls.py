from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('questions/', views.question_view, name='questions'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('results/', views.results_view, name='results_view'),
]
