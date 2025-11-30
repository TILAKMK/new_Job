from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('job/<int:job_id>/', views.JobDetailView.as_view(), name='job_detail'),
    path('job/apply/<int:job_id>/', views.JobApplyView.as_view(), name='apply_job'),
    path('job/<int:job_id>/applicants/', views.view_applicants, name='view_applicants'),
    path('applicant/<int:applicant_id>/<str:action>/', views.update_applicant_status, name='update_applicant_status'),
]
