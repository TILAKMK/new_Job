from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.resume_builder, name='resume_builder'),
    path('resume/preview/', views.resume_preview, name='resume_preview'),
]