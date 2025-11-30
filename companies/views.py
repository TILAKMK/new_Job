from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Company
from .forms import CompanyForm
from jobs.models import Job
from jobs.forms import JobForm
from applicants.models import Applicant

@login_required
def company_profile_view(request):
    if request.user.role != 'employer':
        return redirect('home')
    
    try:
        company = request.user.company
    except Company.DoesNotExist:
        return redirect('companies:create_company')
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies:company_profile')
    else:
        form = CompanyForm(instance=company)
    
    jobs = company.jobs.all()
    return render(request, 'companies/company_profile.html', {'form': form, 'company': company, 'jobs': jobs})

@login_required
def create_company_view(request):
    if request.user.role != 'employer':
        return redirect('home')
    
    if hasattr(request.user, 'company'):
        return redirect('companies:company_profile')
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect('companies:company_profile')
    else:
        form = CompanyForm()
    
    return render(request, 'companies/create_company.html', {'form': form})

@login_required
def post_job_view(request):
    if request.user.role != 'employer':
        return redirect('home')
    
    try:
        company = request.user.company
    except Company.DoesNotExist:
        return redirect('companies:create_company')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            return redirect('companies:company_profile')
    else:
        form = JobForm()
    
    return render(request, 'companies/job_create.html', {'form': form})

@login_required
def job_applicants_view(request, job_id):
    if request.user.role != 'employer':
        return redirect('home')
    
    job = get_object_or_404(Job, id=job_id, company__owner=request.user)
    applicants = job.applicants.all()
    
    paginator = Paginator(applicants, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'companies/job_applicants.html', {'job': job, 'page_obj': page_obj})

@login_required
def update_applicant_status_view(request, applicant_id):
    if request.user.role != 'employer':
        return redirect('home')
    
    applicant = get_object_or_404(Applicant, id=applicant_id, job__company__owner=request.user)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['applied', 'shortlisted', 'rejected', 'accepted']:
            applicant.status = status
            applicant.save()
    
    return redirect('companies:job_applicants', job_id=applicant.job.id)