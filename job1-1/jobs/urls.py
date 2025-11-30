from django.urls import path
from .views import (
    JobListView, JobDetailView, JobCreateView,
    JobApplyView, view_applicants, update_applicant_status
)

app_name = "jobs"

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),

    path('job/<int:job_id>/', JobDetailView.as_view(), name='job_detail'),

    path('job/create/', JobCreateView.as_view(), name='job_create'),

    path('job/<int:job_id>/apply/', JobApplyView.as_view(), name='apply_job'),

    path('job/<int:job_id>/applicants/', view_applicants, name='view_applicants'),

    path('applicant/<int:applicant_id>/<str:action>/',
         update_applicant_status,
         name='update_applicant_status'),
]
