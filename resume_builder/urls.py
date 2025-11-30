from django.urls import path
from .views import resume_builder_view, resume_preview_view

app_name = 'resume_builder'

urlpatterns = [
    path('', resume_builder_view, name='resume_builder'),
    path('preview/', resume_preview_view, name='resume_preview'),
]