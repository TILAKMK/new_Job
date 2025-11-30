from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('job/apply/<int:pk>/', views.ApplyJobView.as_view(), name='apply_job'),
    path('job/create/', views.JobCreateView.as_view(), name='job_create'),
    path('job/update/<int:pk>/', views.JobUpdateView.as_view(), name='job_update'),
    path('job/delete/<int:pk>/', views.JobDeleteView.as_view(), name='job_delete'),
]