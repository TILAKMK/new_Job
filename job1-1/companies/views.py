from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

@login_required
def company_profile(request):
    company = get_object_or_404(Company, owner=request.user)
    return render(request, 'companies/company_profile.html', {'company': company})

@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect('company_profile')
    else:
        form = CompanyForm()
    return render(request, 'companies/job_create.html', {'form': form})

@login_required
def update_company(request):
    company = get_object_or_404(Company, owner=request.user)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_profile')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/job_create.html', {'form': form})