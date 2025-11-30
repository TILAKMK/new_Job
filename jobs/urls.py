from django.urls import path
from .views import job_list_view, job_detail_view, apply_job_view, applied_jobs_view

app_name = 'jobs'

urlpatterns = [
    path('', job_list_view, name='job_list'),
    path('<int:pk>/', job_detail_view, name='job_detail'),
    path('<int:pk>/apply/', apply_job_view, name='apply_job'),
    path('applied/', applied_jobs_view, name='applied_jobs'),
]