from django.urls import path
from .views import (
    company_profile_view,
    create_company_view,
    post_job_view,
    job_applicants_view,
    update_applicant_status_view,
)

app_name = 'companies'

urlpatterns = [
    path('profile/', company_profile_view, name='company_profile'),
    path('create/', create_company_view, name='create_company'),
    path('post-job/', post_job_view, name='post_job'),
    path('job/<int:job_id>/applicants/', job_applicants_view, name='job_applicants'),
    path('applicant/<int:applicant_id>/update-status/', update_applicant_status_view, name='update_applicant_status'),
]