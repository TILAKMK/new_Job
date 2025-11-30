from django.urls import path
from .views import applicant_dashboard_view

app_name = 'applicants'

urlpatterns = [
    path('dashboard/', applicant_dashboard_view, name='applicant_dashboard'),
]