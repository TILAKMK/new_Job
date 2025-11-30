from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('profile/<int:pk>/', views.CompanyDetailView.as_view(), name='company_profile'),
]