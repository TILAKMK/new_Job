from django.urls import path
from . import views

urlpatterns = [
    path('applicants/', views.ApplicantListView.as_view(), name='applicant_list'),
    path('applicants/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicant_detail'),
    path('applicants/<int:pk>/accept/', views.accept_applicant, name='accept_applicant'),
    path('applicants/<int:pk>/reject/', views.reject_applicant, name='reject_applicant'),
]