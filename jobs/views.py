from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Job
from .forms import JobForm, JobSearchForm
from applicants.models import Applicant
from users.models import Profile
from django.contrib import messages

def job_list_view(request):
    jobs = Job.objects.filter(status='approved')
    
    form = JobSearchForm(request.GET)
    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        location = form.cleaned_data.get('location')
        category = form.cleaned_data.get('category')
        
        if keyword:
            jobs = jobs.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
        if location:
            jobs = jobs.filter(location__icontains=location)
        if category:
            jobs = jobs.filter(category__icontains=category)
    
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'jobs/job_list.html', {'page_obj': page_obj, 'form': form})

def job_detail_view(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Applicant.objects.filter(job=job, job_seeker=request.user).exists()
    return render(request, 'jobs/job_detail.html', {'job': job, 'has_applied': has_applied})

@login_required
def apply_job_view(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if request.user.role != 'job_seeker':
        return redirect('home')
    
    if Applicant.objects.filter(job=job, job_seeker=request.user).exists():
        return redirect('jobs:job_detail', pk=pk)
    
    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter', '')
        # Save file to user's profile if a resume was uploaded
        resume_file = request.FILES.get('resume')
        if resume_file:
            profile, _ = Profile.objects.get_or_create(user=request.user)
            profile.resume = resume_file
            profile.save()

        Applicant.objects.create(job=job, job_seeker=request.user, cover_letter=cover_letter)
        messages.success(request, 'Application submitted successfully.')
        return redirect('jobs:applied_jobs')
    
    return render(request, 'jobs/apply_job.html', {'job': job})

@login_required
def applied_jobs_view(request):
    if request.user.role != 'job_seeker':
        return redirect('home')
    
    applications = Applicant.objects.filter(job_seeker=request.user).select_related('job')
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'jobs/applied_jobs.html', {'page_obj': page_obj})